"""
Onion Site Monitor Script with CAPTCHA Bypass

Description:
    This Python script monitors a list of Onion sites for a specific query string periodically. It is designed to bypass CAPTCHA challenges encountered on these sites using the 2Captcha service. If the query string is found on any of the sites, the script sends a notification via Telegram. The script utilizes Selenium with Tor proxy for accessing Onion sites.

Dependencies:
    - Python 3.x
    - Selenium
    - requests

Instructions:
    1. Install the required dependencies via pip:
       ```
       pip install selenium requests
       ```
    2. Obtain a Telegram bot token and chat ID to enable notification functionality.
    3. Obtain a 2Captcha API key for bypassing CAPTCHA challenges.
    4. Prepare a text file containing the list of Onion site URLs to monitor.
    5. Run the script and follow the prompts to input the query string and the path to the URLs file.
    6. The script will periodically (every 15 minutes) check the specified Onion sites for the query string.
    7. If the query string is found on any site, a notification will be sent via Telegram.
    8. CAPTCHA challenges encountered on the sites will be automatically bypassed using the 2Captcha service.

Note: Ensure that Tor is properly configured and running on the system for the Selenium script to work with Onion sites.

"""

import csv
import time
import datetime
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# Telegram bot token and chat ID
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

# 2Captcha API key
api_key_2captcha = 'YOUR_2CAPTCHA_API_KEY'

def solve_captcha_2captcha(api_key, site_key, url):
    """
    Solves CAPTCHA challenges using 2Captcha service.

    Args:
        api_key (str): Your 2Captcha API key.
        site_key (str): The site key extracted from the CAPTCHA challenge.
        url (str): The URL of the page with the CAPTCHA.

    Returns:
        str: The solution to the CAPTCHA challenge.
        None: If unable to solve the CAPTCHA challenge.
    """
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

def search_surface_google(search_term):
    """
    Searches the surface internet using Google search engine.

    Args:
        search_term (str): The query string or dork to search for.

    Returns:
        list: A list of URLs where the search term was found.
    """
    urls = []
    search_url = f"https://www.google.com/search?q={search_term}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and 'http' in href:
                urls.append(href)
    return urls

def search_surface_bing(search_term):
    """
    Searches the surface internet using Bing search engine.

    Args:
        search_term (str): The query string or dork to search for.

    Returns:
        list: A list of URLs where the search term was found.
    """
    urls = []
    search_url = f"https://www.bing.com/search?q={search_term}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and 'http' in href:
                urls.append(href)
    return urls

def check_onion_site(url, search_term, failures, last_notification_sent):
    """
    Checks an Onion site for the presence of a query string or dork and handles CAPTCHA challenges if encountered.

    Args:
        url (str): The URL of the Onion site to check.
        search_term (str): The query string or dork to search for on the site.
        failures (dict): A dictionary tracking the number of consecutive failures for each site.
        last_notification_sent (dict): A dictionary storing the timestamp of the last notification sent for each site.

    Returns:
        tuple: A tuple containing the status code, URL, and comment.
    """
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
        
        # Search for the search term (query string or dork)
        if search_term in driver.page_source:
            print(f"Search term '{search_term}' found in {url}")
            return 0, url, "Search Term Found"  # Search term found
        else:
            print(f"Search term '{search_term}' not found in {url}")
            return 1, None, "Search Term Not Found"  # Search term not found
    except Exception as e:
        print(f"{url} is down: {e}")
        return 1, None, "Site Down"
    finally:
        if driver is not None:
            driver.quit()

def send_notification_to_telegram(url, source):
    """
    Sends a notification to Telegram chat.

    Args:
        url (str): The URL where the search term was found.
        source (str): The source where the search term was found (surface or Onion).
    """
    message = f"Search term found at {url} (Source: {source})."
    
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
    # Get search term from user
    search_term = input("Enter the query string or dork to search for: ")

    # Prompt for search source (Onion, Surface, or Both)
    search_source = input("Enter the search source (Google, Bing, or Both): ").lower()

    # Get path to the urls.txt file from user
    urls_file_path = input("Enter the path to the urls.txt file: ")

    # Read URLs from file
    try:
        with open(urls_file_path, 'r') as file:
            urls = file
