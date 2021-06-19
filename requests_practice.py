import requests

res = requests.get('http://google.com')
# print('response:', res.status_code)
#
# if res.status_code == requests.codes.ok:
#     print('ok')
# else:
#     print('error code :')

#에러 있으면 종료하고 밑에 코드 내보내지 않음 습관적으로 넣기
# res.raise_for_status()
# print('no print')

with open('text.html', 'w', encoding='utf8') as f:
    f.write(res.text)