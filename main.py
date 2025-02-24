# main.py
from scrape import scrape_job_expo  # scrape.py 내 함수 임포트

if __name__ == "__main__":
    # 함수에서 driver를 새로 정의하므로, 여기서는 따로 driver를 주입할 필요는 없습니다.
    df = scrape_job_expo(None)
    print(df)
