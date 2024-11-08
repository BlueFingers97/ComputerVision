import cv2

### 비디오 입출력2 : 카메라(웹캠) 프레임 읽기

cap = cv2.VideoCapture(0)   # 0번 카메라 장치 연결(파일 경로 대신 카메라 장치 인덱스 번호 지정하면 됨. 0부터 시작해서 +1씩)
if cap.isOpened():          # 캡쳐 객체 연결 확인
    while True:
        ret, img = cap.read()   # 다음 프레임 읽기
        if ret:
            cv2.imshow('camera', img) # 다음 프레임 이미지 표시
            if cv2.waitKey(1) != -1:  # 1ms 동안 키 입력 대기(해당 함수는 지정한 시간동안 키 입력이 없으면 -1을 반환함)
                break                 # 아무 키라도 입력이 있으면 프로그램 중지
            else:
                print('no frame')
                break
else:
    print("can't open camera")
cap.release()                         # 자원 반납
cv2.destroyAllWindows()