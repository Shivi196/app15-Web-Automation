from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/Users/misha/PycharmProjects/App15-Web-Automation-Tool-GUI/chromedriver-mac-arm64/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get(url="https://demoqa.com/login")

input(" Presss Enter to close the window")

driver.quit()

