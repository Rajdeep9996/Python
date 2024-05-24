from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.scrapethissite.com/pages/simple/")
    countries = driver.find_elements(By.XPATH, "//h3[@class='country-name']")

    for country in countries:
        print(country.text)

finally:
    driver.quit()