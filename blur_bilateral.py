import cv2
import numpy as np

### 영상 필터3 : 바이레터럴 블러링
# 블러링 필터는 잡음을 제거하는데 효과가 있지만, 경계(엣지)도 흐릿하게 만드는 문제를 가지고 있음
# 바이레터럴 필터는 이 문제를 개선하기 위해 가우시안 필터와 경계 필터 2개를 사용함
# 그 결과, 노이즈는 없고 경계가 비교적 또렷한 영상을 얻을 수 있지만 속도가 느리다는 단점이 있음

img = cv2.imread("./img/gaussian_noise.jpg")

# 가우시안 필터 적용
blur1 = cv2.GaussianBlur(img, (5, 5), 0)

# 바이레터럴 필터 적용
blur2 = cv2.bilateralFilter(img, 5, 75, 75)

# 결과 출력
merged = np.hstack((img, blur1, blur2))
cv2.imshow('bilateral', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()