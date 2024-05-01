Script Description:

This script is designed to search both the surface internet and the dark web for specific queries and notify via Telegram when they're found. It continuously checks the specified URLs for the presence of the query string and also performs surface internet searches periodically.

Step-by-step Explanation:

Imports: The script imports necessary libraries and modules such as csv, time, datetime, requests, selenium, BeautifulSoup, json, and docx for handling CSV files, time-related operations, web scraping, and document generation.

Telegram Bot Configuration: It initializes variables bot_token and chat_id for configuring the Telegram bot, which will be used to send notifications.

Function Definitions: The script defines various functions for writing data to CSV, JSON, and DOCX files, solving CAPTCHA challenges using 2Captcha service, searching the surface internet using Google, Bing, and DuckDuckGo, checking Onion sites for specific queries, performing surface internet searches, and sending notifications to Telegram.

Main Script Execution:
    Input Query and URLs: It prompts the user to enter the query string to search for and the path to the urls.txt file containing the URLs to monitor.
    Reading URLs: It reads the URLs from the specified file and initializes dictionaries to track failures and the last notification sent time for each URL.
    Results Collection: It initializes an empty list results to collect data for CSV, JSON, and DOCX files.
    Main Loop: It enters an infinite loop to continuously monitor the specified URLs and perform searches.
        Checking Onion Sites: It iterates through each URL and checks for the presence of the query string on Onion sites. It updates failure counts, sends notifications, and collects results if the query is found.
        Surface Internet Search: It performs searches on the surface internet using the search_surface function, sends notifications, and collects results if the query is found.
        Data Writing: It writes the collected results to CSV, JSON, and DOCX files.
        Wait: It waits for 15 minutes before the next iteration.

Script Execution: The script continuously executes the main loop until manually interrupted or stopped.

This script provides a comprehensive solution for monitoring specific queries on both the surface internet and the dark web, ensuring timely notifications via Telegram when relevant information is found.
