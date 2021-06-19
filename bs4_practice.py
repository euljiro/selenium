import requests
from bs4 import BeautifulSoup

url ='https://comic.naver.com/index.nhn'
res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # html 문서를 lxml 파서를 통해서 bs4객체로 만들어줌
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음 발견되는 거
# print(soup.a.attrs) # a element의 속성값
# print(soup.a['href']) # a element의 href 속성값
# print(soup.find('a', text='tex///')

f= soup.find('a', attrs={'class':'Nbtn_upload'}) #처음으로 발견되는 엘리먼트, 클래스에 해당 값이 있는 거, 해당 클래스에 속한거
r = soup.find('li', attrs={'class':'rank01'})
# print(r.a.get_text())
# print(r.next_sibling) # 형제 관계로 넘어감
# r2 = r.next_sibling.next_sibling
# r3 = r2.next_sibling.next_sibling
# r4 = r3.previous_sibling.previous_sibling
# p = r4.parent
# print(r2,r3,r4,p)

rank = r.find_next_sibling('li')
ranks = r.find_next_siblings('li')
print(rank.a.get_text(), ranks)