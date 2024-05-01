    Importing Libraries: You import necessary libraries such as csv, time, datetime, requests, and selenium.

    Function Definitions:
        check_onion_site: This function checks a given Onion site for a query string using Selenium with Tor proxy. It returns a status code indicating whether the query was found or not.
        send_notification_to_telegram: This function sends a notification to a Telegram chat using a provided bot token and chat ID.

    User Input: You prompt the user to input the query string to search for and the path to the urls.txt file containing the list of Onion site URLs.

    Reading URLs from File: You read the URLs from the specified file into a list.

    Main Loop:
        You initialize dictionaries to track failures and the time of the last notification for each URL.
        Inside the loop, you iterate over the URLs and check each site for the query string.
        You update the failure count and send a notification if the query is found and if it's been more than a day since the last notification.
        You collect data for the CSV file if the query is found.
        Finally, you write the collected data to a CSV file and sleep for 15 minutes before repeating the process.
Remember to replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with actual values for your Telegram bot. Also, ensure that the Tor proxy is properly configured and running on your system for the Selenium script to work as expected.
