# amazon_webscraping_project

The Amazon Web Scraping Project is a simple Python-based project that demonstrates how to scrape product data from the Amazon.in website. This project is designed solely for learning purposes, focusing on web scraping techniques and how to extract useful information from online e-commerce sites. The scraper collects product details such as the title, price, description, and weight.

**Please note:** This project is meant for educational use only and should be used in accordance with Amazon's terms of service.

## Requirements:
To run this project, you'll need to install the following libraries:
1. `requests`: For making HTTP requests to Amazon's website.
2. `beautifulsoup4`: For parsing HTML and extracting data from the website.
3. `datetime`: For recording the date and time of data extraction.

## Getting Started:
1. Clone the repository.
2. Run the Python program: `web_scraper.py`.
3. Input the Amazon.in product URL and press Enter. The program may not work for other Amazon websites like amazon.com. 
4. The program will extract the product information.

## Limitations:
1. **Amazon's Terms of Service:** Ensure you are aware of Amazon's terms and conditions regarding web scraping. Unauthorized scraping could lead to IP bans or legal actions.
2. **Captcha/Blocking:** Amazon may block IP addresses or require CAPTCHA verification if scraping is done too frequently.
3. **Data Accuracy:** The scraped data may change if the website structure is updated. The script may need updates if Amazon modifies their page layout.