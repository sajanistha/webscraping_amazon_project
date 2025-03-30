from bs4 import BeautifulSoup
import requests
import datetime
from prettytable import PrettyTable

# input the url from Amazon.in
url = input("Enter Amazon.in product URL:")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
response = requests.get(url, headers=headers)
current_time = datetime.datetime.now()

# Create a BeautifulSoup instance
soup = BeautifulSoup(response.text, 'html.parser')

# Create a PrettyTable instance
table = PrettyTable()

# Define the field names based on the results you are displaying
table.field_names = ["Product Details", "Value"]

# Get product title
try:
    title = soup.find('span', id='productTitle')
    title = title.get_text(strip=True)
except:
    title = "NA"

# Get product price
try:
    price = soup.find("span", class_="a-price-whole").get_text(strip=True)
except:
    price = "NA"

# Get product weight
try:
    weight = soup.find('div', id='prodDetails').find(lambda tag: tag.name == 'tr' and 'Item Weight' in tag.text).get_text(strip=True)
except AttributeError:
    try:
        weight = soup.find('div', id='detailBullets_feature_div')
        weight = weight.find(lambda tag: tag.name == 'li' and 'Item Weight' in tag.text).get_text(strip=True)
        weight = weight.strip().replace('\n', '').replace(' ', '')
    except:
        weight = "NA"

# Get product description
def get_product_description():
    try:
        description = soup.find('div', id="productDescription").get_text(strip=True)
        return description
    except AttributeError:
        try:
            description = soup.find(id='feature-bullets').get_text(strip=True)
            return description
        except AttributeError:
            try:
                description = soup.find('div', id='bookDescription_feature_div').get_text(strip=True)
                return description
            except:
                return "NA"

description = get_product_description()

# Add rows to the table
table.add_row(["Current Date and Time", current_time])
table.add_row(["Title", title])
table.add_row(["Price", price])
table.add_row(["Weight", weight])
table.add_row(["Product Description", description])

# Set max width for columns to handle long descriptions
table.max_width = 70 

# Left-align all columns
table.align["Product Details"] = "l"  # Left align the "Product Details" column
table.align["Value"] = "l"  # Left align the "Value" column

# Print the table
print(table)
