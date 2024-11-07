import cv2
import numpy as np

### 영상에서는 물체의 최중심점을 찾는 것이 중요한데, 그것을 사람이나 동물로 비유하면 뼈대와 같은 스켈레톤임
### 거리 변환은 바이너리 스케일 이미지를 대상으로 픽셀 값이 0인 위치로 시작해서 멀어질 때마다 1씩 증가하는 방식으로 가장 먼 픽셀 값이 가장 큰 값을 갖게 함

### 거리 변환

# 이미지(사람의 전신 사진)를 읽어서 바이너리 스케일로 변환
img = cv2.imread('./img/full_body.jpg', cv2.IMREAD_GRAYSCALE)
_, biimg = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 거리 변환
dst = cv2.distanceTransform(biimg, cv2.DIST_L2, 5)
# 거리 값을 0 ~ 255 범위로 정규화(거리 변환 결과는 그 수가 작을 수밖에 없어 영상에 표시되지 않아, 거리 값을 0 ~255 범위로 재조정)
dst = (dst/(dst.max()-dst.min()) * 255).astype(np.uint8)
# 거리 값에 쓰레시홀드로 완전한 뼈대 찾기(뼈대 부분을 더 부각하기 위해)
skeleton = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                 cv2.THRESH_BINARY, 7, -3)

# 결과 출력
cv2.imread('origin', img)
cv2.imshow('dist', dst)
cv2.imshow('skel', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()