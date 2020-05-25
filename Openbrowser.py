from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path=r"C:\Users\Gokul\Downloads\chromedriver_win32\geckodriver.exe")
# driver = webdriver.Chrome(executable_path=r"C:\Users\Gokul\Downloads\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Ie(executable_path=r"C:\Users\Gokul\Downloads\chromedriver_win32\IEDriverServer.exe")

time.sleep(2)
driver.get("https://www.google.com/search?client=firefox-b-d&q=facebook")
print(driver.title)
time.sleep(2)
driver.get("https://www.google.com/search?client=firefox-b-d&q=gmail")
print(driver.title)
time.sleep(4)
driver.back()
print(driver.title)
time.sleep(4)
driver.forward()
print(driver.title)
# print(driver.current_url)
# ele = driver.find_element_by_xpath("(//a[.='Images'])[2]")

# print(driver.page_source)
time.sleep(4)

driver.close()
