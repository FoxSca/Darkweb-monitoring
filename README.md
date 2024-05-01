Description:

The Onion Site Monitor script with CAPTCHA bypass is a Python tool designed to monitor a list of Onion sites (websites accessible via the Tor network) for the presence of a query string or a dork. It periodically checks these sites and sends notifications via Telegram when the specified search term is found. Additionally, it bypasses CAPTCHA challenges encountered on these sites using the 2Captcha service.
Step-by-Step Guide:
Step 1: Overview

The script operates by periodically checking a list of Onion sites for the presence of a specified search term. This search term can be either a specific query string or a dork, which is a combination of keywords used to perform more complex searches.
Step 2: Dependencies

Before using the script, ensure that you have the following dependencies installed:

    Python 3.x
    Selenium
    requests

These dependencies can be installed using pip:

pip install selenium requests

Step 3: Configuration

    Telegram Bot Setup: Obtain a Telegram bot token and chat ID to enable notification functionality. You can create a new bot and obtain its token using the BotFather bot on Telegram.

    2Captcha API Key: Sign up for a 2Captcha account and obtain an API key. This key will be used to solve CAPTCHA challenges programmatically.

Step 4: Prepare URLs File

Prepare a text file containing the list of Onion site URLs that you want to monitor. Each URL should be on a separate line.
Step 5: Running the Script

    Run the script.
    Enter the search term when prompted. This can be either a specific query string or a dork.
    Provide the path to the file containing the list of URLs when prompted.
    The script will start monitoring the specified Onion sites.
    If the search term is found on any site, a notification will be sent via Telegram.
    CAPTCHA challenges encountered on the sites will be automatically bypassed using the 2Captcha service.

Step 6: Monitoring and Notification

The script will continuously monitor the specified Onion sites, checking for the presence of the search term. If the search term is found, a notification will be sent via Telegram. The script will repeat this process every 15 minutes by default.
Step 7: Handling CAPTCHA Challenges

When encountering CAPTCHA challenges on the Onion sites, the script automatically interacts with the 2Captcha service to solve them. This ensures seamless monitoring without manual intervention.
Step 8: Results Logging

The script logs the results of each monitoring session to a CSV file named results.csv. This file contains information about the URLs checked and whether the search term was found or not.
Step 9: Customization

Feel free to customize the script according to your specific requirements. You can adjust the monitoring frequency, notification settings, and error handling as needed.
Step 10: Security Considerations

Ensure that Tor is properly configured and running on your system for the Selenium script to work with Onion sites. Additionally, use the script responsibly and adhere to the terms of service of the websites being monitored.
Example:

    Search Term: onion
    URLs File Path: urls.txt

In this example, the script will monitor the specified Onion sites for the presence of the term "onion" and send notifications via Telegram when it's found.
