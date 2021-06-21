import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

br =webdriver.Chrome(executable_path='./chromedriver')
br.maximize_window()


url = 'https://play.google.com/store/movies/top'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language" : "ko-KR,ko"}
br.get(url)
br.execute_script('window.scrollTo(0,document.body.scrollHeight)')

interval = 2
prev_height = br.execute_script('return document.body.scrollHeight')

while True:
    br.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(interval)
    current_height= br.execute_script('return document.body.scrollHeight')
    if current_height == prev_height:
        break
    prev_height = current_height # 트루되면 종료

print('완료')


soup = BeautifulSoup(br.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class':['ImZGtf mpg5gc', 'Vpfmgd']})
print(len(movies))

for movie in movies:
    title= movie.find('div',  attrs={'class':'WsMG1c nnK0zc'}).get_text()
    sale = movie.find('span', attrs={'class':'SUZt4c djCuy'})
    if sale:
        sale = sale.get_text()
    else:
        continue

    price  =movie.find('span', attrs={'class': 'VfPpfd ZdBevf i5DZme'}).get_text()
    link = movie.find('a', attrs={'class':'JC71ub'})['href']
    print(title, sale, price, link)


