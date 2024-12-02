import cv2, time
import numpy as np

### 경계 검출2 - 케니 엣지(한 가지 필터를 사용하는 것이 아니라 4단계 알고리즘을 적용한 잡음에 강한 엣지 검출기로 가장 많이 사용됨)

img = cv2.imread("./img/sudoku.jpg")

# 케니 엣지 적용
edges = cv2.Canny(img, 100, 200)

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()