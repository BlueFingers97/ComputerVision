import cv2

### 이미지 읽기 : OpenCV 사용해서 이미지 읽고 화면에 표시하기

img_file = "./img/girl.jpg" # 표시할 이미지 위치(경로)
img = cv2.imread(img_file)  # 이미지를 읽어서 변수에 할당하는 함수

if img is not None:
    cv2.imshow('IMG', img)  # 읽은 이미지 화면에 표시(IMG가 창 제목)
    cv2.waitKey()           # 이 함수는 키보드의 입력이 있을 때까지 대기함
    cv2.destroyAllWindows() # 이 함수는 표시한 창을 모두 닫고 프로그램을 종료함
else:
    print('No Image File')


# cv2.imread() 함수는 이미지를 읽을 때 모드를 지정할 수 잇음
# img = cv2.imread(파일명, cv2.IMREAD_GRAYSCALE)
# cv2.IMREAD_COLOR : 컬러(RGB) 스케일로 읽기, 기본 값
# cv2.IMREAD_UNCHANGED : 파일 그대로 읽기
# cv2.IMREAD_GRAYSCALE : 흑백 스케일로 읽기