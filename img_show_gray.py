import cv2

### 이미지 피일을 흑백(그레이 스케일)로 화면에 표시하기

img_file = './img/girl.jpg'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 읽기

if img is not None:
    cv2.imshow('IMG_GRAY', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No Image File')