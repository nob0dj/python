from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from chromedriver import installer # 실행용
from chromedriver.installer import get_chromedriver_path # 상위 디렉토리 모듈 가져오기
from selenium.webdriver.common.by import By

from models import WebtoonRank, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///naver_api.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

path = get_chromedriver_path()
print('path =', path)

day = 'tue'
url = f'https://comic.naver.com/webtoon?tab={day}'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service) # Chrome(path) 구버젼, Chrome(service) 최신버젼방식

sleep(3)
driver.get(url)

# 별점순 클릭하기
sleep(5)
btn_sort_by_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/button[4]')
print(btn_sort_by_star) # <selenium.webdriver.remote.webelement.WebElement (session="f3243061b252598683e639c2caca6778", element="67b371e3-d843-49de-89a4-bca0fe77f900")>
btn_sort_by_star.click()


sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

li_list = soup.select('.component_wrap .item')
# print(all_webtoons)


for i, li in enumerate(li_list):
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    star = li.find('span', class_='Rating__star_area--dFzsb').find('span', class_='text').text
    print(f'{i + 1} : {star} {title}')

    new_rank = WebtoonRank(day, i + 1, star, title)
    session.add(new_rank)

session.commit()


driver.close()
