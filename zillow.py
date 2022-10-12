import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from pprint import pprint

chrome_driver_path = "/Users/adu/development/selenium/chromedriver"


class ZillowBot:

    def __init__(self, path):
        self.path = path
        # self.driver = webdriver.Chrome(executable_path=self.path)

    def extract_data(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        data = requests.get(
            "https://www.zillow.com/bloomington-il/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A40.66369909921535%2C%22east%22%3A-88.74306279980468%2C%22south%22%3A40.30543742532676%2C%22west%22%3A-89.2168482001953%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A23742%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D",
            headers=header).content
        extracted_items = []
        soup = BeautifulSoup(data, 'html.parser')
        unorderd_list = soup.find(name="ul", class_="with_constellation")
        listed_items = unorderd_list.find_all("li")

        for item in listed_items:
            # print(item)
            try:
                article = item.find(name="article")
                p_data = article.find(name="div", class_="property-card-data")
                print(p_data)
                url = p_data.find(name="a")['href']
                property = p_data.find(name="address").getText()
                price = p_data.find(name="span").getText()
                print(url, property, price)

                extracted_items.append({'name': property, 'price': price, 'link': url})
            except AttributeError:
                pass

        return extracted_items

    def fill_form(self):
        pass


zw = ZillowBot(path=chrome_driver_path)
print(zw.extract_data())
