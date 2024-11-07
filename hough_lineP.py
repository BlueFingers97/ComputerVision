import cv2
import numpy as np

### 허프 변환 : 직선이나 원 같은 간단한 모양을 식별

# 허프 선 변환
img = cv2.imread('./img/sudoku.jpg')
img2 = img.copy()

# 그레이 스케일로 변환 및 엣지 검출
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edges = cv2.Canny(imgray, 50, 200) # 경계 검출의 케니 엣지 검출

# 확률 허프 변환 적용
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, None, 20, 2)
for line in lines:
    # 검출된 선 그리기
    x1, y1, x2, y2 = line[0]
    cv2.line(img2, (x1, y1), (x2, y2), (0, 255, 0), 1)

merged = np.hstack((img, img2))
cv2.imshow('Probability hough line', merged)
cv2.waitKey()
cv2.destroyAllWindows()