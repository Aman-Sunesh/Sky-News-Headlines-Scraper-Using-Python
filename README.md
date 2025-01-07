
# Sky News Headlines Scraper

## Overview
The Sky News Headlines Scraper is a Python script designed to automatically extract and save the latest news headlines from the Sky News website. Utilizing the `requests` and `BeautifulSoup` libraries, this tool provides a simple and efficient way to gather up-to-date news information for personal use or further analysis.

## Prerequisites
Before you can run this application, ensure you have the following installed:
- Python 3.8 or higher
- `requests` library
- `BeautifulSoup4` library

## Installation

### Python Installation
Download and install Python from [python.org](https://www.python.org/downloads/).

### Library Installation
Use `pip` to install the required Python libraries:
```bash
pip install requests beautifulsoup4
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/Sky-News-Headlines-Scraper-Using-Python.git
cd Sky-News-Headlines-Scraper-Using-Python
```

## Usage
To run the application, navigate to the application directory and run:
```bash
python python_web_scraping.py
```

## Functionality

### Scrape Headlines
- **Target Website**: Sky News (`https://news.sky.com/`)
- **Extracted Data**: News headlines along with the timestamp of when they were scraped.
- **Output**: Saves the scraped headlines to a CSV file named `headlines.csv`.

### CSV File Structure
- **Headline**: The text of the news headline.
- **Scraping Time**: The date and time when the headline was scraped.

## Important Notes
- Ensure that the Sky News website's structure has not changed. If the HTML structure changes, you may need to update the class names or tags used in the script.
- The script creates or overwrites the `headlines.csv` file in the same directory as the script. Ensure you have write permissions for this directory.

## Troubleshooting

### Requests Library Errors
- **Issue**: `requests.exceptions.RequestException`
- **Solution**: Check your internet connection and ensure that the Sky News website is accessible. Verify that the URL is correct.

### BeautifulSoup Parsing Errors
- **Issue**: Unable to find headlines or empty CSV file.
- **Solution**: Inspect the Sky News website to confirm that the HTML structure (tags and classes) used in the script matches the current structure of the website. Update the `class_` parameter in the `find_all` method if necessary.

### CSV File Not Created or Not Populated
- **Issue**: The `headlines.csv` file is not created or is empty after running the script.
- **Solution**: Ensure that the script has the necessary permissions to write to the directory. Check for any errors printed in the console and address them accordingly.

### General Errors
- **Issue**: Unexpected errors or exceptions.
- **Solution**: Review the error messages printed in the console to identify the issue. Common problems include network connectivity issues, changes in website structure, or missing libraries. Ensure all prerequisites are installed and up to date.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or additional features.

## Acknowledgments
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
