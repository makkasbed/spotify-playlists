import os

import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
actual_price = float(price_without_currency)
print(actual_price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

budget = 200

if actual_price < budget:
    message = f"{title} is now {price}"

    with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
        connection.starttls()
        result = connection.login(os.getenv("SMTP_EMAIL"), os.getenv("SMTP_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("SMTP_EMAIL"),
            to_addrs=os.getenv("SMTP_TO_EMAIL"),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )