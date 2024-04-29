# 50자 이상 리뷰 수집 에러 수정, 페이지 버튼 클릭 로직 수정

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import traceback
import sys
from pyvirtualdisplay import Display

# Linux 환경에서 selenium 실행 시 필요한 옵션
display = Display(visible=0, size=(1920, 1080))
display.start()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

# MongoDB 연결 설정
client = MongoClient('mongodb://192.168.1.162:27017/')
db = client['fts']
reviews_collection = db['reviews']

# 리뷰 저장 함수
def saveDatabase(product_id, reviews):
    for review_text, review_date, rank in reviews:
        document = {
            "productId": product_id,
            "contents": review_text,
            "date": review_date,
            "rank": rank
        }
        reviews_collection.insert_one(document)
        print(f"Added review with _id: {document['_id']}")

# 리뷰 수집 함수
def collectReviews(product_id):
    start_time = datetime.now()
    url = f"https://search.shopping.naver.com/catalog/{product_id}?section=review"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-nclick='N=a:rev.rec']")))
        driver.find_element(By.CSS_SELECTOR, "a[data-nclick='N=a:rev.rec']").click()

        reviews_collected = []
        page_number = 1

        while len(reviews_collected) < 100:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.reviewItems_list_review__q726A p.reviewItems_text__XrSSf")))
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            review_blocks = soup.select("ul.reviewItems_list_review__q726A li")

            for block in review_blocks:
                review_text = ' '.join(block.select_one("p.reviewItems_text__XrSSf").stripped_strings)
                review_date = block.select_one("div.reviewItems_etc_area__3VUjt span.reviewItems_etc__9ej69:nth-of-type(4)").get_text().strip()
                rank = block.select_one("div.reviewItems_etc_area__3VUjt span.reviewItems_average__0kLWX").get_text().strip()
                rank = int(rank.replace("평점", ""))

                if len(review_text) >= 50:
                    reviews_collected.append((review_text, review_date, rank))
                    if len(reviews_collected) % 10 == 0:
                        print(f"{len(reviews_collected)}개의 리뷰 수집중...")

            if len(reviews_collected) >= 100:
                break

            # 다음 페이지 버튼 클릭 처리
            page_number += 1
            next_page_locator = (By.CSS_SELECTOR, f"div.pagination_pagination__JW7zT > a[data-nclick='N=a:rev.page,r:{page_number}']")
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(next_page_locator))
                next_page_button = driver.find_element(*next_page_locator)
                driver.execute_script("arguments[0].click();", next_page_button)
                next_page_button.click()
            except TimeoutException:
                print(f"다음 페이지 버튼을 찾을 수 없습니다. 페이지 번호: {page_number}")
                break

        saveDatabase(product_id, reviews_collected)

    except Exception as e:
        traceback.print_exc()
    finally:
        driver.quit()
        end_time = datetime.now()
        print(f"수집 완료. 총 소요 시간: {end_time - start_time}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        product_id_input = sys.argv[1]
        collectReviews(product_id_input)
    else:
        print("Insufficient arguments provided. Please provide Product ID.")
