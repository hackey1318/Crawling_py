import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
in_text = input("검색하고 싶은 정보는 : ")
url = "https://www.google.com/search?q="+parse.quote(in_text)+"&oq="+parse.quote(in_text)
req = urllib.request.urlopen(url)
res = req.read()
soup = BeautifulSoup(res,'html.parser') # BeautifulSoup 객체생성
keywords = soup.find_all('h3','LC201b') # 데이터에서 태그와 클래스를 찾는 함수
print(keywords)
