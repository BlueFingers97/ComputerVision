import cv2

### 비디오 입출력 : 동영상 파일 재생
# OpenCV는 동영상 파일이나 컴퓨터에 연결한 카메라로부터 연속된 이미지 프레임을 읽을 수 있는 API를 제공함

video_file = './img/big_buck.avi'  # 동영상 파일 경로

cap = cv2.VideoCapture(video_file)  # 동영상 캡쳐 객체 생성(동영상 파일이나 컴퓨터에 연결한 카메라 장치로부터 영상 프레임을 읽기 위해서는 해당 객체가 필요함)
if cap.isOpened():                  # 객체 생성 후 파일이나 카메라에 제대로 연결되었는지 확인(캡쳐 객체가 지정한 파일로 정상적으로 초기화 됐으면 True 반환함)
    while True:                     # 연속해서 파일 프레임 읽기 위한 무한 루프
        ret, img = cap.read()           # 다음 프레임 읽기(Boolean과 Numpy 배열 객체를 쌍으로 갖는 튜플(ret, img) 객체 반환)
        if ret:                         # ret 값이 true면 프레임 읽기 정상(읽기에 성공)
            cv2.imshow("video_file", img) # 화면에 동영상을 표시
            cv2.waitKey(25)             # 25ms 지연(40fps로 가정) -> cv2.waitKey()는 FPS(Frames Per Second)에 맞게 영상 재생 속도를 조정함
        else:                           # 다음 프레임 읽을 수 없음
            break                       # 재생 완료
else:
    print("can't open video")           # 캡쳐 객체 초기화 실패
cap.release()                           # 프로그램 종료 전 releas() 함수 호출해서 캡쳐 자원 반납
cv2.destroyAllWindows()