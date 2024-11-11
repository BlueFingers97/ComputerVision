import cv2

### 이미지 프로세싱 : 컬러 스페이스 변환
img = cv2.imread('./img/girl.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #BGR을 그레이 스케일로 변경(인자를 지정하면 컬러 이미지를 그레이 스케일로 변환함)
cv2.imshow('original', img)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()