from bs4 import BeautifulSoup
import requests


# naver -> 웹툰 -> 웹툰 -> 화요웹툰
resp = requests.get('https://comic.naver.com/webtoon')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)

all_webtoons = soup.find_all('div', class_='component_wrap')
print(all_webtoons) # []] 원하는 내용들이 안나옴
