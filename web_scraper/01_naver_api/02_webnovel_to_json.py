import json

from bs4 import BeautifulSoup
import requests

resp = requests.get('https://novel.naver.com/webnovel/weekday')
soup = BeautifulSoup(resp.text, 'html.parser')

# find 매칭되는 첫번째 결과 반환 (존재하지 않는 경우 None 반환)
# ranking_wrapper = soup.find('div', class_='component_section')
ranking_wrapper = soup.find(id='integrationRaking')

item_list = ranking_wrapper.find_all('li', class_='item')

webnovels = list(); # 빈 배열 생성

for item in item_list:
    # 순위 가져오기
    rank = item.p.text.strip() # item하위 첫번째 p태그의 text, strip()을 통해 문자열의 앞부분과 뒷부분에 있는 공백 문자(스페이스, 탭, 개행 등)을 제거하여 문자열의 시작과 끝을 정리

    # 제목 가져오기
    # title = item.find_all('p')[1].find('span', class_='title').text
    # title = item.select('span.title')[0].text # list 반환
    title = item.select_one('span.title').text # <class 'bs4.element.Tag'> 반환
    print(f'{rank}위 : {title}')

    # dict로 생성후 list에 추가
    tmp = dict()
    tmp['rank'] = rank
    tmp['title'] = title
    print(tmp)
    webnovels.append(tmp)

# dump 아니고 dumps
result_json = json.dumps(webnovels, ensure_ascii=True)
with open('webnovels.json', 'w', encoding='utf-8') as f:
    f.write(result_json)

result = dict()
result['status'] = '성공'
result['webnovels'] = webnovels
result_json = json.dumps(result, ensure_ascii=False)
with open('result_webnovels.json', 'w', encoding='utf-8') as f:
    f.write(result_json)







