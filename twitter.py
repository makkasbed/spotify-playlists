import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/adu/development/selenium/chromedriver"


class InternetSpeedTwitterBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)

        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        pass


speed_bot = InternetSpeedTwitterBot(chrome_driver_path)
speed_bot.get_internet_speed()
speed_bot.tweet_at_provider()
