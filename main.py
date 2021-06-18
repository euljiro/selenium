from selenium import webdriver
import time

# Webdriver 실행
dr = webdriver.Chrome(executable_path='./chromedriver')
# Webdriver에서 네이버 페이지 접속
dr.get('https://www.naver.com/')
# 로그인 버튼 클릭
ele = dr.find_element_by_class_name('link_login')
ele.click()

# id. password
dr.find_element_by_id('id').send_keys('ma_natsu03')
dr.find_element_by_id('pw').send_keys('Bluesky0190!')
dr.find_element_by_id('log.login').click()

time.sleep(3)

# 새로 입력
dr.refresh()
dr.find_element_by_id('id').clear()
dr.find_element_by_id('id').send_keys('hi')

print(dr.page_source)
dr.quit()

# ele=dr.find_element_by_class_name('clssName) //클래스 이름으로 찾기침
# ele=dr.find_element_by_id('id') //id로 찾기
# ele = dr.fine_element_by_xpath("copy and paste")
# ele.click()//클릭하기
# dr.back() // 뒤로 돌아가기
# dr.forward() // 앞으로 가기
# dr.refresh() // 새로고
# ele.quit()//전체 닫기
# ele.close()//현재 창 닫기기
# from selenium.webdriver.common.keys import Keys // 키 입력
# ele.send_keys('keykey') //''안에 입력
# ele.send_keys(Keys.ENTER) // 엔
