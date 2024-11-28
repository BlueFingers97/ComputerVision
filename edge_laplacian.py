import cv2
import numpy as np

### 경계 검출 - 라플라시안 필터(미분 결과를 다시 미분하는 2차 미분을 적용해 경계를 더 확실히 검출할 수 있음)
# 경계 검출은 영상에서 배경과 전경을 분리하는 작업

img = cv2.imread("./img/sudoku.jpg")

# 라플라시안 필터 적용
edge = cv2.Laplacian(img, -1)

# 결과 출력
merged = np.hstack((img, edge))
cv2.imshow('Laplacian', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

