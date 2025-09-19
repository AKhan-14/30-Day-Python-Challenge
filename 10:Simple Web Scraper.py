# The Challenge: Write a script that scrapes the titles of the top stories from a news website.

# Step 0: Setup - Installing Your Tools
# pip install requests, pip install beautifulsoup4

# Step 1: The Request - Fetching the Web Page

"""
import requests
url = "https://www.bbc.co.uk/news"
response = requests.get(url)
# print(response.status_code)

# if response.status_code == 200:
#     print("Success!")
# elif response.status_code == 404:
#     print("Not Found.")

print(response.text)
"""

# Step 2: The Inspection - Finding the Headlines in the HTML
# <h3> is the headlines format in html using inspect element

# Step 3: The Parser - Extracting the Titles

"""
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.co.uk/news"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
results = soup.find_all("h3")
# print(len(results))
for item in results:
    print(item.text.strip())
"""

# Step 4: The Refinement - Cleaning the Output

import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.co.uk/news"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
results = soup.find_all("h3")
# print(len(results))

unique_headlines = []
seen_headlines = set()

for item in results:
    headline = item.text.strip()
    if headline not in seen_headlines:
        unique_headlines.append(headline)
        seen_headlines.add(headline)
    elif headline in seen_headlines:
        continue

print("--- Top BBC News Headlines ---")
for i, headline in enumerate(unique_headlines, start=1):
        print(f"{i}. {headline}")



