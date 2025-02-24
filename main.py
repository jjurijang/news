# main.py

from selenium import webdriver as wb
from job_expo import scrape_job_expo

if __name__ == "__main__":
    driver = wb.Chrome()
    try:
        df = scrape_job_expo(driver)
        print(df.head())  # 크롤링한 결과 확인 로그
    finally:
        driver.quit()
