import cv2
import numpy as np

### 영상 필터 : 블러링(영상의 초점이 맞지 않는 것처럼 흐린하게 만드는 것)

# 영상 필터는 영상 처리에서 입력 값에 원하지 않는 값은 걸러내고 원하는 결과만 얻는다는 의미임
# 필터는 영상을 흐릿하게 만들거나 또렷하게 만들기도 해서 영상의 품질을 높임
# 엣지(경계)를 검출하고 엣지의 방향을 알아내는 등 객체 인식과 분리의 기본이 되는 정보를 계산함

file_name = "./img/taekwonv1.jpg"
img = cv2.imread(file_name)

# blur() 함수로 블러링(주변 픽셀 값들의 평균을 적용하면 블러링이 적용됨)
blur1 = cv2.blur(img, (10, 10))    # cv2.blur()함수는 커널의 크기만 지정하면 평균 커널을 생성해서 블러링 적용한 영상을 만들어냄
# boxFilter() 함수로 블러링 적용
blur2 = cv2.boxFilter(img, -1, (10, 10))

# 결과 출력
merged = np.hstack((img, blur1, blur2))
cv2.imshow('blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
