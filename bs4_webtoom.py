# import requests
# from bs4 import BeautifulSoup
#
# url ='https://comic.naver.com/webtoon/weekday.nhn'
# res= requests.get(url)
# res.raise_for_status()
#
# soup = BeautifulSoup(res.text, 'lxml') # html 문서를 lxml 파서를 통해서 bs4객체로 만들어줌
# #웹툰 전체 목록
# cartoons = soup.find_all('a', attrs={'class':"title"})
# # a element의 클래스 속성이 title 인 모든 element 반환
# for cartoon in cartoons:
#     print(cartoon.get_text())


import requests
from bs4 import BeautifulSoup

url ='https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu'
res= requests.get(url)

soup = BeautifulSoup(res.text, 'lxml') # html 문서를 lxml 파서를 통해서 bs4객체로 만들어줌
# cartoons = soup.find_all('td', attrs={'class':'title'})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# print(title)
# print('https://comic.naver.com' + link)
# 만화 제목과 링
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'https://comic.naver.com'+ cartoon.a['href']
#     print(title, link)크
# 평균 평점 구하기
t_rate = 0
cartoons = soup.find_all('div', attrs={'class': 'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    t_rate += float(rate)

print('total:', t_rate)
print('average :' , t_rate / len(cartoons))