import cv2

### 이미지 프로세싱2 : 관심영역 복제 및 새 창 띄우기

img = cv2.imread('./img/sunset.jpg')

x=320; y=150; w=50; h=50
roi = img[y:y+h, x:x+w]     # roi 지정
img2 = roi.copy()           # roi 배열 복제(관심영역으로 지정한 배열을 복제해서 새로운 배열 생성)

img[y:y+h, x+w:x+w+w] = roi # 새로운 좌표에 roi 추가, 태양 2개 만들기
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0, 255, 0)) # 2개의 태양 영역에 사각형 표시

cv2.imshow("img", img)      # 원본 이미지 출력
cv2.imshow("roi", img2)     # roi만 따로 출력

cv2.waitKey(0)
cv2.destroyAllWindows()