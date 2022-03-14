import requests
from bs4 import BeautifulSoup
# import lxml
import smtplib

TARGET_PRICE = 90.00
MY_EMAIL = "rainbowkittencuties@yahoo.com"
PASSWORD = "Bkkflblfpaiqclfeg"


def main():
    url = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/" \
          "dp/B08PQ2KWHS/ref=dp_fod_1?pd_rd_i=B08PQ2KWHS&psc=1"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                      "KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,lb;q=0.8,fr;q=0.7"
    }

    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, "lxml")

    # price = float(soup.find(class_="a-offscreen").text.split("$")[1])
    price = soup.find(class_="a-offscreen").getText()
    price_text = price.split("$")[1]
    price_float = float(price_text)

    product_name = soup.find(name="span", id="productTitle").getText().strip()

    message = f"{product_name} is now {price}!\n{url}"

    if price_float < TARGET_PRICE:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Amazon Price Alert\n\n{message}"
            )


if __name__ == '__main__':
    main()
