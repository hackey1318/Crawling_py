import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
#현재는 URL을 고정했기 때문에 Repactoring해서 사용하는 코드 작성하기
#url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html, 'html.parser')

#title = soup.find_all(class_='sh_blog_title')
#for i in title:
#    print(i.attrs['title'])
#    print(i.attrs['href'])
#    print()


#Repactoring한 코드
baseURL = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusURL = input('검색어를 입력하세요 : ')
url = baseURL + urllib.parse.quote(plusURL)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')
for i in title:
    print(i.attrs['title']+'\t'+i.attrs['href']+'\n')