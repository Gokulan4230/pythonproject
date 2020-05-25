from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\Gokul\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://en-gb.facebook.com/")
driver.implicitly_wait(10)
link_add = driver.find_element_by_xpath("//a[.='Forgotten account?']")
wait = WebDriverWait(driver, 10)
print(wait.until(EC.presence_of_element_located((By.XPATH,"//a[.='Forgotten account?']"))))
time.sleep(3)
# s = Select(link_add)
# s.select_by_value()
action = ActionChains(driver)
action.key_down(Keys.CONTROL).click(link_add).key_down(Keys.CONTROL).perform()
windows = driver.window_handles
driver.switch_to.window(windows[1])
assert "Facebook" in driver.title
time.sleep(3)
print("Test case is pass")
driver.close()