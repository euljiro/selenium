import requests

url = 'http://naver.com'
headers = {"User_Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open('naver.html', 'w', encoding='utf8') as f:
    f.write(res.text)