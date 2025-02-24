from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
import pandas as pd
def scrape_job_expo(driver):
    # 데이터를 쌓아둘 리스트
    url="https://www.naver.com/"
    driver = wb.Chrome()
    driver.get(url)

    search = driver.find_element(By.ID, "query")
    search.send_keys("취업박람회 일정")
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    
    # 1) "테마" 드롭다운 열기 버튼 찾기 & 클릭
    theme_button = driver.find_elements(By.CSS_SELECTOR,"span.menu._text")
    theme_button[2].click()
    time.sleep(1)
    science_button = driver.find_elements(By.CSS_SELECTOR,"a.item_link")
    science_button[3].click()
    
    title_list = []
    date_list = []
    place_list = []
        
    while True:
        try:
            # 현재 페이지에서 채용박람회 정보를 수집
            titles = driver.find_elements(By.CSS_SELECTOR, "div.title")
            dates = driver.find_elements(By.CSS_SELECTOR, "dd.no_ellip")
            places = driver.find_elements(By.CSS_SELECTOR, "dd.no_ellip + dt + dd")
            
            # 각 항목별 텍스트 추출
            for i in range(len(titles)):
                titles = driver.find_elements(By.CSS_SELECTOR, "div.title")
                dates = driver.find_elements(By.CSS_SELECTOR, "dd.no_ellip")
                places = driver.find_elements(By.CSS_SELECTOR, "dd.no_ellip + dt + dd")
                title_list.append(titles[i].text)
                date_list.append(dates[i].text)
                place_list.append(places[i].text)

            # 다음 페이지 버튼 클릭 (없거나 활성화되지 않으면 예외 발생 가능)
            title_list2 = [item for item in title_list if item.strip() != ""]
            date_list2 = [item for item in date_list if item.strip() != ""]
            place_list2 = [item for item in place_list if item.strip() != ""]

            next_button = driver.find_element(By.CSS_SELECTOR, "a.pg_next.on")
            next_button.click()
            time.sleep(1)
        
        except Exception as e:
            # 예외 발생 시 크롤링 중단
            print(f"크롤링 중단 (예외 발생): {e}")
            break

    # 공백 문자열 제거

    # DataFrame 생성
    df = pd.DataFrame({
        "박람회": title_list2,
        "기간": date_list2,  # 요청에 따라 하이퍼링크 등 다른 방식으로 저장 가능
        "장소": place_list2,
    })

    # CSV 저장
    csv_filename = "job_expo.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
    
    return df
