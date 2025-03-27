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

# Locate the username,password and login button of Home page
username = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'password')))
# login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'login')))
login = driver.find_element(By.ID,'login')

# Fill in username,password and click login button

username.send_keys("pythonuser")
password.send_keys("Python!n16")
# login.click()
driver.execute_script('arguments[0].click();',login)


# Locate the Elements dropdown and Textbox and click them

Elements = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
Elements.click()
Textbox = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'item-0')))
Textbox.click()

# Locate the Form fields and Submit Button of Elements tab's Text Box page
FullName = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
Email = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userEmail')))
Current_Address = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
Permanent_Address = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
Submit = driver.find_element(By.ID,'submit')


# Fill in the details of form fields  and click submit button

FullName.send_keys("Misha Sharma")
Email.send_keys("connecttoshivi@gmail.com")
Current_Address.send_keys("Jannat,Shiv Vihar")
Permanent_Address.send_keys("Jannat,Shiv Vihar")
driver.execute_script('arguments[0].click();',Submit)


input(" Presss Enter to close the window")
driver.quit()

