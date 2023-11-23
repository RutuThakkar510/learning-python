import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("https://www.scrapethissite.com/pages/")
# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(response.content, "html.parser")
print(soup.name)

# Extract the title of the webpage
title = soup.title.string
print(f"Title: {title}")

# Extract all the links from the webpage
para = soup.find_all("p")
print(para)

for p in para:
    print(p.text)
    print(p['class'])

links = soup.find_all("a")
for link in links:
    print(link["href"])