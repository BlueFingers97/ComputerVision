import cv2

### 이미지 프로세싱 : 관심영역 지정(ROI, Region Of Interest)

# 전체 이미지에서 연산과 분석의 대상이 되는 영역만 지정하고 떼어내는 것을 관심영역 지정한다고 한다.

img = cv2.imread('./img/sunset.jpg')

x=320; y=150; w=50; h=50    # roi 좌표(시작좌표와 크기)
roi = img[y:y+h, x:x+w]     # roi 지정

print(roi.shape)            # roi shape, (50, 50, 3) - 세로 픽셀수, 가로 픽셀수, 색채널
cv2.rectangle(roi, (0, 0), (h-1, w-1), (0, 255, 0)) # roi 전체에 사각형 그리기(해당 영역에 사각형 표시, 선 그리기 위해 -1픽셀)
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()