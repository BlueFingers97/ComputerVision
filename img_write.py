import cv2

### 이미지 저장하기 : 읽어 들인 이미지를 다시 파일로 저장
img_file = './img/girl.jpg'
save_file = './img/girl_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)     # 이미지를 파일로 저장, 포맷은 확장에 따름
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.imwrite(파일 경로, img) : 이미지를 파일에 저장
# file_path : 저장할 파일 경로 이름
# img : 저장할 영상, Numpy 배열