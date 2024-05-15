import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT_URL = "Your desired amazon product link"
TARGET_PRICE = 350
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your password"

headers = {
    "User-Agent": "your-user-agent. Use (https://myhttpheader.com/)",
    "Accept-Language": "your-accept-language. Use (https://myhttpheader.com/)"
}
response = requests.get(url=PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

product_name = soup.find(name="span", id="productTitle").text.strip()
price_string = soup.find(name="span", class_="a-offscreen")

current_price = float(price_string.text.split("$")[1])

if current_price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Your Tracked Amazon Product is on Sale\n\n{product_name} is now ${current_price}\n{PRODUCT_URL}"
        )
