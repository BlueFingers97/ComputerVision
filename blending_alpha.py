import cv2

### 이미지 프로세싱 : 알파 블렌딩

alpha = 0.5 # 합성에 사용할 알파 값(각 영상에 적용할 가중치)

# 합성에 사용할 영상 읽기
img1 = cv2.imread('./img/wing_wall.jpg')
img2 = cv2.imread('./img/yate.jpg')

# addWeighted() 함수로 알파 블렌딩 적용(각 영상의 픽셀 값에 각각 50%씩 곱해서 새로운 영상 생성)
dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
cv2.imshow('cv2.addWeighted', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()