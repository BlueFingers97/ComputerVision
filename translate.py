import cv2
import numpy as np

### 기하학적 변환 : 이동

img = cv2.imread('./img/fish.jpg')
rows, cols = img.shape[0:2]  # 영상의 크기

dx, dy = 100, 50        # 이동할 픽셀 거리

#1. 변환 행렬 생성
mtrx = np.float32([[1, 0, dx],
                [0, 1, dy]])

#2. 단순 이동(cv2.warpAffine()함수는 원본 영상을 행렬에 따라 변환해서 결과 이미지 크기로 만들어서 반환함)
# -- cv2.warpAffine() 함수로 영상을 이동
# -- 출력 영상의 크기를 원래 크기보다 이동한 만큼 더 크게 지정해서 잘리지 않게 함
# -- 영상의 좌측과 윗 부분은 원래 없던 픽셀이 추가돼서 외곽 영역이 검게 표현됨
dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))

#3. 탈락된 외곽 픽셀을 파랑색으로 보정(외곽 영역을 고정 값 파란색(255, 0, 0)으로 보정함
dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None,
                       cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255, 0, 0))

#4. 탈락된 외곽 픽셀을 원본을 반사 시켜서 보정(원본 영상을 거울에 비친 것처럼 복제해서 보정함)
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None,
                       cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('original', img)
cv2.imshow('trans', dst)
cv2.imshow('BORDER_CONSTANT', dst2)
cv2.imshow('BORDER_FEFLECT', dst3)
cv2.waitKey()
cv2.destroyAllWindows()