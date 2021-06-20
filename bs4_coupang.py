import requests
import re
from bs4 import BeautifulSoup

url ='https://www.coupang.com/np/search?component=&q=%EC%95%84%EC%9D%B4%EB%A7%A5'
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" }
res= requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('li', attrs={'class':re.compile('^search-product')})
# print(items[0].find('div', attrs={'class':'name'}).get_text())
for item in items:
    #광고 제품 제외
    ad_badge = item.find('span', attrs={'class':'ad-badge-text'})
    if ad_badge:
        print('no ad')
        continue
    name= item.find('div', attrs={'class':'name'}).get_text()
    #애플 제품 제외
    if 'Apple' in name:
        print('no apple')
        continue

    price = item.find('strong', attrs={'class':'price-value'}).get_text()

    #평점 100개 이상 4.5 이상
    rate= item.find('em', attrs={'class':'rating'})
    if rate:
        rate = rate.get_text()
    else:
        print('평점 없음')

    rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print('평점 수 없음')
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
         print(name, price, rate, rate_cnt)