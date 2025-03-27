from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver,options & service
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')
service = Service("/Users/misha/PycharmProjects/App15-Web-Automation-Tool-GUI/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(options=chrome_options,service=service)

# Load the page
driver.get(url="https://demoqa.com/login")

# Locate the username,password and login button
username = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'password')))
# login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'login')))
login = driver.find_element(By.ID,'login')

# Fill in username,password and click login button

username.send_keys("pythonuser")
password.send_keys("Python!n16")
# login.click()
driver.execute_script('arguments[0].click();',login)

input(" Presss Enter to close the window")

driver.quit()

