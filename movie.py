import requests_practice
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/top'
res= requests_practice.get(url)