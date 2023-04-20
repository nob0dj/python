from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from chromedriver import installer # 실행용
from chromedriver.installer import get_chromedriver_path # 상위 디렉토리 모듈 가져오기


path = get_chromedriver_path()
print('path =', path)

url = 'https://comic.naver.com/webtoon?tab=tue'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)


sleep(3)
driver.get(url)

sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

li_list = soup.select('.component_wrap .item')
# print(all_webtoons)

for li in li_list:
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    star = li.find('span', class_='Rating__star_area--dFzsb').text
    print(f'{star} "{title}"')

driver.close()
