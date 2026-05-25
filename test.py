# from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

print("Chrome berhasil dibuka")

time.sleep(5)

driver.quit()
