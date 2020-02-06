import pyautogui

#pyautogui.moveTo(x좌표, y좌표, 이동시간)
#pyautogui.click(x좌표, y좌표)  #자리로 바로 가서 클릭

#pyautogui.locateOnScreen('이미지 파일이름')
#none이 나오면 opencv-python을 설치해야
#이미지파일의 x,y,크기,크기의 4개의 데이터 값을 추출
#4개의 값은 가공을 거쳐 pyautogui.center()를 이용해 center값으로 만들기
#pyautogui.locateCenterOnScreen('이미지 파일이름')은 한 번에 center값으로

#pyautogui.screenshot('이미지파일 이름', region=(x,y,크기,크기))로
#프로그램으로 이미지 파일 생성
