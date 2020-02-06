from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
t = 'script'
baseURL = 'https://www.google.com/search?q='
plusURL = input('무엇을 검색할까요? : ')
plus2URL = input('1. 학술지 2. 논문 3. 책 4. 강의 : ')
if plus2URL == "1":
    text_word = "학술지"
    t+="h"
elif plus2URL == "2":
    text_word = "논문"
    t+="n"
elif plus2URL == "3":
    text_word = "책"
    t+="b"
elif plus2URL == "4":
    text_word = "강의"
    t+="l"
t+=".csv"
f=open(t,'w')
url = baseURL + quote_plus(plusURL+" & "+text_word)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.r')
for i in r:
    try:
        f.write(i.select_one('.LC20lb').text + ',' + i.a.attrs['href'] + '\n')
    except:
        continue

driver.close()