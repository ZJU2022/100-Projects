from selenium import webdriver
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(executable_path='venv/bin/chromedriver'))
browser.get('https://www.baidu.com/')