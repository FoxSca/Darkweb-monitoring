"""
Onion Site Monitor Script

This script periodically checks a list of Onion sites for a specific query string
and sends notifications via Telegram if the query is found. It utilizes Selenium
with Tor proxy for accessing Onion sites.

Dependencies:
- Python 3.x
- Selenium
- requests

Instructions:
1. Install the required dependencies via pip:
2. Configure a Telegram bot and obtain the bot token and chat ID.
3. Provide the path to a text file containing the list of Onion site URLs.
4. Run the script. It will check the sites periodically and send notifications
when the specified query string is found.

Note: Ensure that Tor is properly configured and running on the system for the
Selenium script to work with Onion sites.
"""

import csv
import time
import datetime
import requests
from selenium import webdriver

# Telegram bot token and chat ID
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

# 2Captcha API key
api_key_2captcha = 'YOUR_2CAPTCHA_API_KEY'

def solve_captcha_2captcha(api_key, site_key, url):
    captcha_url = f"https://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl={url}&json=1"
    response = requests.get(captcha_url)
    if response.status_code == 200:
        request_id = response.json()['request']
        for _ in range(20):  # Poll for CAPTCHA solving status
            time.sleep(10)
            resp = requests.get(f"https://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1")
            if resp.status_code == 200:
                if resp.json()['status'] == 1:
                    return resp.json()['request']
        return None
    else:
        return None

def check_onion_site(url, query, failures, last_notification_sent):
    driver = None
    
    try:
        proxy_address = "127.0.0.1:9150"
        capabilities = {
            'proxy': {
                'socksProxy': proxy_address,
                'socksVersion': 5,
            }
        }
        
        driver = webdriver.Firefox(capabilities=capabilities)
        
        driver.get(url)
        time.sleep(5)

        # Check if CAPTCHA is present
        if "google.com/recaptcha" in driver.page_source:
            site_key = driver.find_element_by_css_selector("div[data-sitekey]").get_attribute("data-sitekey")
            captcha_solution = solve_captcha_2captcha(api_key_2captcha, site_key, url)
            if captcha_solution:
                driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{captcha_solution}';")
                driver.execute_script("document.getElementById('g-recaptcha-response').style.display='';")
                driver.execute_script("document.getElementById('g-recaptcha-response').style.visibility='visible';")
                driver.execute_script("document.getElementById('g-recaptcha-response').style.height='auto';")
                time.sleep(5)  # Wait for CAPTCHA to be solved
                driver.find_element_by_css_selector("button[type='submit']").click()
                time.sleep(5)  # Wait for page to load after CAPTCHA
            else:
                raise Exception("Failed to solve CAPTCHA")
        
        query_found = query in driver.page_source
        if query_found:
            print(f"Query found in {url}")
            return 0, url, "Query Found"  # Query found
        else:
            print(f"Query not found in {url}")
            return 1, None, "Query Not Found"  # Query not found
    except Exception as e:
        print(f"{url} is down: {e}")
        return 1, None, "Site Down"
    finally:
        if driver is not None:
            driver.quit()

def send_notification_to_telegram(url):
    message = f"Query string found at {url}."
    
    send_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    
    response = requests.post(send_message_url, data=payload)
    if response.ok:
        print(f"Message sent to Telegram chat {chat_id}")
    else:
        print("Failed to send message to Telegram")

if __name__ == "__main__":
    # Get query string from user
    query = input("Enter the query string to search for: ")

    # Get path to the urls.txt file from user
    urls_file_path = input("Enter the path to the urls.txt file: ")

    # Read URLs from file
    try:
        with open(urls_file_path, 'r') as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        exit()

    failures = {url: 0 for url in urls}
    last_notification_sent = {url: datetime.datetime.now() for url in urls}

    csv_data = []  # Collect data for CSV

    while True:
        for url in urls:
            fail_count, found_url, comment = check_onion_site(url, query, failures, last_notification_sent)

            # Update failure count
            if fail_count == 1:
                failures[url] += 1
            else:
                failures[url] = 0

            # Send notification and update last notification time
            if fail_count == 0 and (datetime.datetime.now() - last_notification_sent[url]).days >= 1:
                send_notification_to_telegram(found_url)
                last_notification_sent[url] = datetime.datetime.now()

            # Add data to CSV if query found
            if fail_count == 0:
                csv_data.append([url, comment])

        # Write data to CSV
        with open('results.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['URL', 'Comment'])
            csv_writer.writerows(csv_data)

        time.sleep(900)  # Check every 15 minutes
