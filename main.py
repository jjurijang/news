# main.py

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
import pandas as pdfrom job_expo import scrape_job_expo

if __name__ == "__main__":
    driver = wb.Chrome()
    try:
        df = scrape_job_expo(driver)
        print(df.head())  # 크롤링한 결과 확인 로그
    finally:
        driver.quit()
