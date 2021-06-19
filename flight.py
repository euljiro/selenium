from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

br = webdriver.Chrome(executable_path='./chromedriver')

url ='https://flight.naver.com/flights'
br.get(url)

br.find_element_by_link_text('가는날 선택').click()

#이번달, 다음달 27일 선
br.find_elements_by_link_text('27')[0].click()
br.find_elements_by_link_text('27')[0].click()

#지역 선택
br.find_element_by_xpath("//*[@id='recommendationList']/ul/li[4]").click()
br.find_element_by_link_text('항공권 검색').click()

try:
    ele = WebDriverWait(br, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]")))
    #성공했을때
    print(ele.text)
finally:
    br.quit()

#결과 출력
# ele = br.find_element_by_xpath("//*[@id='recommendationList']/ul/li[4]")
# print(ele.text)