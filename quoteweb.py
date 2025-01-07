import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# URL
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

# Parse the HTML
soup = BeautifulSoup(r.content, 'html5lib')

# Check if we are able to find the section with quotes
table = soup.find('div', attrs={'id': 'all_quotes'})
if table is None:
    print("Couldn't find the quotes section. Check if the HTML structure has changed.")
else:
    print("Quotes section found.")

# List to store quotes
quotes = []

# Loop through and extract quotes
for row in table.findAll('div', attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    theme = row.find('h5')  # Find the theme (quote category)
    if theme:
        quote['theme'] = theme.text
    else:
        print("Theme not found for a quote.")
    
    url = row.find('a')  # Find the link
    if url and 'href' in url.attrs:
        quote['url'] = url['href']
    else:
        print("URL not found for a quote.")
    
    img = row.find('img')  # Find the image
    if img and 'src' in img.attrs:
        quote['img'] = img['src']
    else:
        print("Image not found for a quote.")
    
    # Extract quote lines and author from the alt text
    if img and 'alt' in img.attrs:
        alt_text = img['alt']
        if " #" in alt_text:
            quote['lines'] = alt_text.split(" #")[0]
            quote['author'] = alt_text.split(" #")[1]
        else:
            quote['lines'] = alt_text
            quote['author'] = "Unknown"
    else:
        print("Alt text (quote and author) not found.")
    
    quotes.append(quote)

# If quotes were found, save to CSV
if quotes:
    filename = 'inspirational_quotes.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['theme', 'url', 'img', 'lines', 'author'])
        writer.writeheader()
        for quote in quotes:
            writer.writerow(quote)





    
