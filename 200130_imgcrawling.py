from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

baseURL = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
plusURL = input('검색어를 입력하시오 :')
url = baseURL + quote_plus(plusURL)
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

n=1
for i in img:
    imgURL = i['data-source']
    with urlopen(imgURL) as f:
        #wb는 이미지 파일을 write하는 것이기이에 바이너리파일로 만드는 것
        #naver이미지에서 나오는 수에 맞추어 for문 작동
        with open('./img/' + plusURL + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n+=1
    print(imgURL)
print('다운로드 완료')