import cv2

### 이미지 연산 : 이퀄라이즈
### 픽셀 각각의 값이 전체 분포에 차지하는 비중에 따라 분포를 재분배하므로 명암 대비를 개선하는데 효과적임

# 1. 대상 영상을 그레이 스케일로 읽기
img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)

# 2. OpenCV API로 이퀄라이즈 히스토그램 적용
img3 = cv2.equalizeHist(img)

cv2.imshow('Before', img)
cv2.imshow('cv2.equalizeHist()', img3)
cv2.waitKey()
cv2.destroyAllWindows()
