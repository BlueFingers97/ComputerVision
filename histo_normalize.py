import cv2

### 이미지 연산 : 노멀라이즈
### 원래 기준이 서로 다른 값을 같은 기준이 되게 만드는 것으로, 특정 구간으로 노멀라이즈하면 특정 부분에 몰려 있는 값을 전체 영역으로 골고루 분포하게 할 수 있음

# 1. 그레이 스케일로 영상 읽기
img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)

# 2. OpenCV API를 이용한 정규화(cv2.normalize() 함수로 노멀라이즈 적용)
# 구간 노멀라이즈를 사용하려면 cv2.NORM_MINMAX 플래그 상수를 사용하고 대상 구간 값(0, 255)을 전달함
# 중앙에 몰려 있던 픽셀들의 분포가 전체적으로 고르게 퍼져서 화질이 개선됨
img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('Before', img)
cv2.imshow('cv2.normalize()', img_norm2)
cv2.waitKey()
cv2.destroyAllWindows()