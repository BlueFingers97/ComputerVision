import numpy as nu, cv2

### 이미지 프로세싱 : 이미지 연산(차영상)
# 영상에서 영상을 빼기 연산하면 두 영상의 차이, 즉 변화를 알 수 있는데 이것을 차영상이라고 함

# 연산에 필요한 영상을 읽고 그레이스케일로 변환
img1 = cv2.imread('./img/robot_arm1.jpg')
img2 = cv2.imread('./img/robot_arm2.jpg')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 두 영 상의 절대값 차 연산
diff = cv2.absdiff(img1_gray, img2_gray)

# 차 영상을 극대화 하기 위해 쓰레시홀드 처리 및 컬러로 변환
# 1. 1보다 큰 값은 모두 255로 바꾸고(이미지를 검정색과 흰색으로 표현하는 걸 바이너리 이미지라고 함), 스레시홀딩은 여러 값을 경계점을 기준으로 두 부류로 나누는 것으로 바이너리 이미지를 만드는 방법임
# 2. 색상을 표현하기 위해 컬러 스케일로 바꿈
_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)
diff_red =  cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
diff_red[:,:,2] = 0

# 두 번째 이미지에 변화 부분 표시(원본 이미지의 어느 부분이 변경되었는지 표현해 주기 위해서 cv2.bitwise_xor()연산 진행)
# 원본 이미지는 배경이 흰색이므로 255를 가지고 있고, 차영상은 차이가 있는 빨간색 영역을 가지고 있어 XOR 연산을 하면 차영상 부분이 합성이 됨
spot = cv2.bitwise_xor(img2, diff_red)

# 결과 영상 출력
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.imshow('spot', spot)
cv2.waitKey()
cv2.destroyAllWindows()