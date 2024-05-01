Step 1: Overview

The Onion Site Monitor script is designed to periodically check a list of Onion sites (websites accessible via the Tor network) for a specific query string. If the query string is found on any of the sites, the script sends a notification via Telegram. Additionally, the script is capable of bypassing CAPTCHA challenges encountered on these sites using the 2Captcha service.
Step 2: Dependencies

Before using the script, ensure that you have the following dependencies installed:

    Python 3.x
    Selenium
    requests

You can install these dependencies via pip:

pip install selenium requests

Step 3: Configuration

    Telegram Bot: Obtain a Telegram bot token and chat ID to enable notification functionality. You can create a new bot and obtain its token using the BotFather bot on Telegram.

    2Captcha API Key: Sign up for a 2Captcha account and obtain an API key. This key will be used to solve CAPTCHA challenges programmatically.

Step 4: Prepare URLs File

Prepare a text file containing the list of Onion site URLs that you want to monitor. Each URL should be on a separate line.
Step 5: Running the Script

    Run the script.
    Input the query string to search for when prompted.
    Provide the path to the file containing the list of URLs when prompted.
    The script will start monitoring the specified Onion sites.
    If the query string is found on any site, a notification will be sent via Telegram.
    CAPTCHA challenges encountered on the sites will be automatically bypassed using the 2Captcha service.

Step 6: Monitoring and Notification

The script will continuously monitor the specified Onion sites, checking for the presence of the query string. If the query string is found, a notification will be sent via Telegram. The script will repeat this process every 15 minutes by default.
Step 7: Handling CAPTCHA Challenges

When encountering CAPTCHA challenges on the Onion sites, the script automatically interacts with the 2Captcha service to solve them. This ensures seamless monitoring without manual intervention.
Step 8: Results Logging

The script logs the results of each monitoring session to a CSV file named results.csv. This file contains information about the URLs checked and whether the query string was found or not.
Step 9: Customization

Feel free to customize the script according to your specific requirements. You can adjust the monitoring frequency, notification settings, and error handling as needed.
Step 10: Security Considerations

Ensure that Tor is properly configured and running on your system for the Selenium script to work with Onion sites. Additionally, use the script responsibly and adhere to the terms of service of the websites being monitored.
