from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation :

    def __init__(self):
        # Define driver,options & service
        chrome_options = Options()
        chrome_options.add_argument('--disable-search-engine-choice-screen')

        download_path = os.getcwd()
        prefs = {'download.default_directory':download_path}
        chrome_options.add_experimental_option('prefs',prefs)

        service = Service("/Users/misha/PycharmProjects/App15-Web-Automation-Tool-GUI/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(options=chrome_options,service=service)

    def login(self,user_name,user_pswd):
        # Load the page
        self.driver.get(url="https://demoqa.com/login")

        # Locate the username,password and login button of Home page

        username = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        # login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'login')))
        login = self.driver.find_element(By.ID, 'login')

        # Fill in username,password and click login button

        username.send_keys(user_name)
        password.send_keys(user_pswd)
        # login.click()
        self.driver.execute_script('arguments[0].click();', login)

    def fill_form(self,fullname,email,ca,pa):
         # Locate the Elements dropdown and Textbox and click them
        Elements = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
        Elements.click()
        Textbox = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'item-0')))
        Textbox.click()

        # Locate the Form fields and Submit Button of Elements tab's Text Box page
        FullName = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
        Email = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'userEmail')))
        Current_Address = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
        Permanent_Address = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
        Submit = self.driver.find_element(By.ID,'submit')

        # Fill in the details of form fields  and click submit button

        FullName.send_keys(fullname)
        Email.send_keys(email)
        Current_Address.send_keys(ca)
        Permanent_Address.send_keys(pa)
        self.driver.execute_script('arguments[0].click();',Submit)

    def download_file(self):

        # Locate the Upload and Data tab and Download button

        Upload_Download = self.driver.find_element(By.ID,'item-7')
        self.driver.execute_script('arguments[0].click();',Upload_Download)
        Download_button = self.driver.find_element(By.ID,'downloadButton')
        self.driver.execute_script('arguments[0].click();',Download_button)

    def close(self):
        input(" Presss Enter to close the window")
        self.driver.quit()


if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login("pythonuser","Python!n16")
    web_automation.fill_form("Misha Sharma","connecttoshivi@gmail.com","Jannat,Shiv Vihar","Jannat,Shiv Vihar")
    web_automation.download_file()
    web_automation.close()



