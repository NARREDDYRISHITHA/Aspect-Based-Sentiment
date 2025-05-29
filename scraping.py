import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize an empty list to hold all reviews
all_reviews = []

# Function to extract reviews from a single page
def extract_reviews(url, retries=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Accept-Language': 'en-IN,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.amazon.in/',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all review elements
        reviews = soup.find_all('span', {'data-hook': 'review-body'})

        # Append reviews to the list
        for review in reviews:
            all_reviews.append(review.get_text(strip=True))

        # Find the link to the next page
        next_page = soup.find('li', {'class': 'a-last'})
        if next_page and next_page.find('a') and 'href' in next_page.find('a').attrs:
            next_url = 'https://www.amazon.in' + next_page.find('a')['href']
            return next_url
        else:
            return None

    except requests.exceptions.RequestException as e:
        if retries > 0:
            print(f"Error fetching the URL: {e}. Retrying in 5 seconds...")
            time.sleep(5)
            return extract_reviews(url, retries - 1)
        else:
            print(f"Error fetching the URL: {e}. No more retries left.")
            return None

# Initial URL for the first page of reviews
url = 'https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/product-reviews/B09G9HD6PD/'  # Replace with the product URL

# Loop through all pages
page_number = 1
while url:
    print(f"Scraping page {page_number}...")
    url = extract_reviews(url)
    page_number += 1
    time.sleep(2 + 2 * page_number)  # Increase delay as you go through more pages

# Convert the reviews list into a DataFrame
df = pd.DataFrame(all_reviews, columns=['Review'])

# Save the DataFrame to a CSV file
output_file = 'amazon_reviews.csv'
df.to_csv(output_file, index=False)

print(f"Scraped {len(all_reviews)} reviews and saved to '{output_file}'")