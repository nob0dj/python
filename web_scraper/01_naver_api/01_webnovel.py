from bs4 import BeautifulSoup
import urllib.request
import requests

# naver -> 웹툰 -> 웹소설
# 1. urllib.request.urlopen 방식
# resp = urllib.request.urlopen('https://novel.naver.com/webnovel/weekday')
# soup = BeautifulSoup(resp, 'html.parser')
# print(soup)

# 2. requests.get 방식
resp = requests.get('https://novel.naver.com/webnovel/weekday')
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

# find 매칭되는 첫번째 결과 반환 (존재하지 않는 경우 None 반환)
# ranking_wrapper = soup.find('div', class_='component_section')
ranking_wrapper = soup.find(id='integrationRaking')
# print(ranking_wrapper)

item_list = ranking_wrapper.find_all('li', class_='item')
# print(item_list)

for item in item_list:
    # 순위 가져오기
    rank = item.p.text.strip() # item하위 첫번째 p태그의 text, strip()을 통해 문자열의 앞부분과 뒷부분에 있는 공백 문자(스페이스, 탭, 개행 등)을 제거하여 문자열의 시작과 끝을 정리

    # 제목 가져오기
    # title = item.find_all('p')[1].find('span', class_='title').text
    # title = item.select('span.title')[0].text # list 반환
    title = item.select_one('span.title').text # <class 'bs4.element.Tag'> 반환
    print(f'{rank}위 : {title}')
