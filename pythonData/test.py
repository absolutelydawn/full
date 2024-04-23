#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
import json

# WebDriver 초기화
driver = webdriver.Chrome()

# MongoDB 클라이언트 초기화 및 데이터베이스 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['review_database']
reviews_collection = db['reviews']

def save_to_database(product_id, reviews_json):
    reviews_data = json.loads(reviews_json)
    document = {"product_id": product_id, "reviews": reviews_data}
    result = reviews_collection.insert_one(document)
    saved_document = reviews_collection.find_one({"_id": result.inserted_id})
    return json.dumps(saved_document, default=str, ensure_ascii=False)

def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def collect_reviews(product_id, query):
    url = f"https://search.shopping.naver.com/catalog/{product_id}?query={query}"
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.floatingTab_on__2FzR0 a[aria-selected="true"] strong'))
        )
        review_tab = driver.find_element(By.CSS_SELECTOR, 'li.floatingTab_on__2FzR0 a[aria-selected="true"] strong')
        if review_tab.text == "쇼핑몰리뷰":
            review_tab.click()
        scroll_down(driver)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        reviews = [p.text for p in soup.select('div.reviewItems_review__DqLYb div.reviewItems_review_text__dq0kE p.reviewItems_text__XrSSf')]
        reviews_json = json.dumps(reviews)
        return save_to_database(product_id, reviews_json)
    except Exception as e:
        print(f"Failed to process URL for product ID {product_id}: {e}")
        return []

# 사용자 입력 받기
product_id_input = input("Enter Product ID: ")
query_input = input("Enter Query: ")

# 리뷰 수집 및 결과 출력
result_json = collect_reviews(product_id_input, query_input)
print(f"Collected Reviews for Product ID {product_id_input}: {result_json}")

# WebDriver 종료
driver.quit()