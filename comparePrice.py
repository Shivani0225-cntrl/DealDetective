from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
import time

prod = "SONY ZV-E10L"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40)
driver.get("https://www.flipkart.com")
wait.until(EC.visibility_of_element_located((By.XPATH, '(//button)[2]')))
# time.sleep(2)
close = driver.find_element(By.XPATH, "(//button)[2]")
close.click()
first_tab = driver.current_window_handle
inputprod1 = driver.find_element(By.NAME, "q")
inputprod1.send_keys(prod)
search1 = driver.find_element(By.XPATH, '//form//button')
search1.click()
wait.until(EC.visibility_of_element_located((By.XPATH, '(//a//div[@class="_30jeq3"])[1]')))
flipPrice = driver.find_element(By.XPATH, '(//a//div[@class="_30jeq3"])[1]')
priceFlip = flipPrice.text
priceFlip = priceFlip[1:]
print(priceFlip)
driver.execute_script('''window.open("https://www.amazon.in/", "_blank");''')
second_tab = driver.window_handles[1]
driver.switch_to.window(second_tab)
inputprod2 = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
inputprod2.send_keys(prod)
search2 = driver.find_element(By.ID, "nav-search-submit-button")
search2.click()
amazPrice = driver.find_element(By.XPATH, '(//span[@class="a-price-whole"])[1]')
priceAmaz = amazPrice.text
if priceAmaz > priceFlip:
    print("Flipkart is cheaper as compared to Amazon.\nFlipkart price: Rs. "+priceFlip)
elif priceFlip > priceAmaz:
    print("Amazon is cheaper as compared to Flipkart.\nAmazon price: Rs. "+priceAmaz)
else:
    print("Both Amazon and Flipkart prices are equal.\nProduct price: Rs. "+priceAmaz)
driver.close()
