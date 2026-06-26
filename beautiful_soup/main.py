from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver import ActionChains
import time

driver = webdriver.Safari()
products: list = [] # Storing the name of products
prices: list = [] # Storing the price of products

# Call the built-in safari driver since it's inbuilt into safari

def main():
    print("Hello from Spec Crawler!")
    driver.get('https://jiji.ng/cars?query=macbooks')
    no_change_count = 0
    scroll_count = 0

    # Scrolling down the page
    while True:
        if scroll_count >= 15:
            break
        page_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        new_page_height = driver.execute_script("return document.body.scrollHeight")
        if page_height == new_page_height:
            no_change_count += 1
            if no_change_count >= 3:
                break
        else:
            no_change_count = 0
        scroll_count += 1

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # Finding all the required elements, using the class attribute
    for a in soup.find_all(attrs={"class": 'b-adverts-gallery-listing__item js-advert-list-item'}):
        name = a.find('div', attrs={'class': 'b-list-advert-base__data__title'})
        price = a.find('div', attrs={'class': 'b-list-advert-base__data__price'})
        products.append(name.text if name else 'N/A')
        prices.append(price.text if price else 'N/A')

    # Create a DataFrame that holds the data. Columns are Product and Price
    df = pd.DataFrame({'Product': products, 'Price': prices})
    df = df[df['Product'].str.contains('MacBook|Laptop', case=False)]  # filter here
    df.to_csv('products.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
