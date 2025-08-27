

import time
import requests
import sqlite3
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import subprocess 

def FindDomain_autocompleteclearbit(name):
    FinalDomains = []
    req = requests.get(f"https://autocomplete.clearbit.com/v1/companies/suggest?query={name}")
    data = req.json()
    for d in data:
        if "https://" not in str(d['domain']) :
          if "www." not in str(d['domain']):   
            FinalDomains.append('https://'+'www.'+d['domain'])
          else:
            FinalDomains.append('https://'+d['domain'])
    return FinalDomains






def FindDomain_ducksearch(name):
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(f"https://duckduckgo.com/?q={name}")
        time.sleep(2)
        links = [a.get_attribute("href") for a in driver.find_elements(By.CSS_SELECTOR, '[data-testid="result-title-a"]')]
        return links
    finally:
        driver.quit()
