import cv2

### 비디오 입출력4 : 여러 프레임을 저장할 때는 cv2.VideoWriter() API 사용

cap = cv2.VideoCapture(0)   #0번 카메라 연결
if cap.isOpened:
    file_path = './record.avi'  # 저장할 파일 경로 이름
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 인코딩 포맷 문자
    fps = 30.0                  # FPS, 초당 프레임 수
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))        # 프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # VideoWriter 객체 생성(저장할 파일 이름, 인코딩 포맷 문자, FPS, 프레임 크기)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording', frame)
            out.write(frame)                # 파일 저장
            if cv2.waitKey(int(1000/fps)) != -1:
                break
            else:
                print("no frame!")
                break
        out.release()                       # 파일 닫기
    else:
        print("can't open camera!")
    cap.release()
    cv2.destroyAllWindows()