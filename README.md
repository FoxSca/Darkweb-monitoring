Step-by-Step Description:
1. Description of Script:

    This script enables users to search the surface internet for a specified query string or dork using Google and Bing search engines.
    It integrates web scraping capabilities to retrieve search results and provides options for handling CAPTCHA challenges.
    Search results are logged, and notifications are sent to a Telegram chat.

2. Dependencies:

    Python 3.x
    requests
    selenium
    BeautifulSoup

3. Example Usage:
3.1. Running the Script:

    Execute the script in a Python environment.

bash

python surface_internet_search.py

3.2. Entering Search Query:

    You will be prompted to enter the query string or dork to search for.

bash

Enter the query string or dork to search for: vulnerability disclosure

3.3. Choosing Search Source:

    Select the search source (Google, Bing, or Both) when prompted.

bash

Enter the search source (Google, Bing, or Both): Both

3.4. Providing URL File Path:

    Enter the path to the urls.txt file containing Onion site URLs.

bash

Enter the path to the urls.txt file: /path/to/urls.txt

4. Monitoring Output:

    Monitor the script output for search results and notifications.
    Example output:

plaintext

Search term 'vulnerability disclosure' found in https://example.com (Source: Google).
Message sent to Telegram chat YOUR_CHAT_ID

Example:

Let's say you want to search for the query "cybersecurity news" using both Google and Bing search engines, and you have a file named urls.txt containing Onion site URLs. Here's how you would use the script:

bash

Enter the query string or dork to search for: cybersecurity news
Enter the search source (Google, Bing, or Both): Both
Enter the path to the urls.txt file: /path/to/urls.txt

Then, you would monitor the script output to see the search results and notifications as they occur.
