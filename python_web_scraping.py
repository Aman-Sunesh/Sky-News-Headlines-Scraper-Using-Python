import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os


# URL of the website
url = 'https://news.sky.com/'

# CSV file name
csv_file = 'headlines.csv'

# Define the headers for the CSV file
csv_headers = ['Headline', 'Scraping Time']



try:
    # Make the HTTP request to the website
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    counter = 1

    # Open the CSV file in append mode
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(csv_headers)

        # Extract headlines, keeping only those with the keep_class
        for headline in soup.find_all("a", class_= "ui-story-headline"):
            if headline.text.strip():
                headline_text = f"{counter}. {headline.text.strip()}\n"  # Print the numbered stripped text of the headline
                counter += 1  # Increment the counter for the next headline

                # Get the current time for the scraping timestamp
                scraping_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([headline_text, scraping_time])

    print(f"Headlines have been successfully saved to '{csv_file}'.")


except requests.RequestException as e:
    print(f"Error during requests to {url} : {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")