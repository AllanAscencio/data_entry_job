import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import json

# --------------- CONSTANTS ---------------------- #

CHROME_DRIVER_PATH = "\chromedriver_win32\chromedriver.exe"

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A" \
             "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
             "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A" \
             "%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse" \
             "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D" \
             "%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min" \
             "%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "

GOOGLE_FORM = "https://forms.gle/CWygPMayS3ZHVCfbA"


# -------------------- ZILLOW --------------------- #

response = requests.get(ZILLOW_URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "es,en-GB;q=0.9,en;q=0.8,de;q=0.7"})

zillow_rents = response.text

soup = BeautifulSoup(zillow_rents, "html.parser")

test = soup.findAll("script", attrs={"type": "application/json"})
rent_data = test[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")
rent_data = json.loads(rent_data)
rent_links = []
rent_addresses = []
rent_prices = []

# ----------------- Obtain url of all houses -----------------#
for i in rent_data["cat1"]["searchResults"]["listResults"]:
    if i['detailUrl'].startswith("http"):
        rent_links.append(i['detailUrl'])
    elif i['detailUrl'].startswith("/b"):
        rent_links.append(f"https://www.zillow.com{i['detailUrl']}")

# ------------------ Obtain prices of all houses -----------------#
for i in rent_data["cat1"]["searchResults"]["listResults"]:
    try:
        rent_prices.append(i['price'].rstrip("+/mo"))
    except:
        rent_prices.append(i['units'][0]['price'].rstrip("+"))

# ----------------- Obtain addresses of all houses -----------------#

for i in rent_data["cat1"]["searchResults"]["listResults"]:
    rent_addresses.append(i['address'])


# ---------------------- SELENIUM CLASS -------------------- #

class InstaFollower:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options,
                                       service=Service(executable_path="chromedriver.exe", log_path="NUL"))


    def fill_form(self):
        self.driver.get("https://forms.gle/CWygPMayS3ZHVCfbA")
        time.sleep(2)
        for each in range(0, 40):
            self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(f"{rent_addresses[each]}")
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(f"{rent_prices[each]}")
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(f"{rent_links[each]}")
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
            time.sleep(2)


bot = InstaFollower()
bot.fill_form()