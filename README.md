1. Purpose:

    This script is designed to monitor both the dark web (Onion sites) and the surface internet (Google, Bing, DuckDuckGo) for the presence of a specified query string or dork.
    It automates the process of periodically checking a list of Onion site URLs and performing user research queries on surface search engines.

2. Features:

    Dark Web Monitoring: The script utilizes Selenium, a web scraping tool, to navigate through Onion sites and search for the specified query string.
    Surface Internet Search: It interacts with surface search engines like Google, Bing, and DuckDuckGo to search for the query string and capture relevant URLs from the search results.
    Notification System: When the query string is found either on Onion sites or in the surface search results, the script sends notifications to a designated Telegram chat.
    Logging: It maintains a log of the search results in a CSV file for future reference and analysis.

3. Example Usage:

    Scenario 1: Monitoring Dark Web Activity
        Input: The user specifies a query string like "illegal activities" and provides a list of Onion site URLs in a file named urls.txt.
        Output: The script continuously checks the specified Onion sites for the presence of the query string. If found, it sends a notification to the Telegram chat.

    Scenario 2: Researching Surface Internet
        Input: The user inputs a query string or dork like "data breach" and selects surface search engines (Google, Bing, DuckDuckGo).
        Output: The script conducts searches on the selected surface search engines and captures relevant URLs from the search results. It then sends notifications for any matches found.

4. Benefits:

    Efficiency: Automates the monitoring process, saving time and effort compared to manual checks.
    Timeliness: Provides real-time notifications, enabling prompt action in response to identified content.
    Comprehensive Coverage: Monitors both the dark web and surface internet, offering a holistic view of online activity related to the specified query.

5. Use Cases:

    Security Monitoring: Organizations can use this script to monitor for mentions of sensitive keywords or phrases related to security threats on both the dark web and surface internet.
    Brand Reputation Management: Companies can track discussions about their brand or products across various online platforms to manage reputation and address potential issues promptly.

6. Implementation:

    The script utilizes Python's Selenium library for web scraping and interacts with the Telegram API for notifications.
    It employs CSV file handling for logging search results and utilizes requests library for making HTTP requests to surface search engines.

7. Customization:

    Users can customize the query strings, search sources, and notification settings according to their specific monitoring requirements.
    Additional functionalities or integrations, such as email notifications or alternative search engines, can be incorporated based on user needs.

8. Maintenance:

    Regular updates may be required to adapt to changes in web page structures, CAPTCHA mechanisms, or search engine algorithms.
    Users are encouraged to review and adjust the script parameters periodically to ensure optimal performance and relevance to their monitoring objectives.
