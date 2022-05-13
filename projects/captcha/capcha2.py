import CaptchaCracker as cc

# 타겟 이미지 크기
img_width = 150
img_height = 40
# 타겟 이미지 라벨 길이
max_length = 6
# 타겟 이미지 라벨 구성요소
characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

# 모델 가중치 파일 경로
weights_path = "model/weights2.h5"
# 모델 적용 인스턴스
AM = cc.ApplyModel(weights_path, img_width, img_height, max_length, characters)

# 타겟 이미지 경로
target_img_path = "interpark/cpt (1).png"

# 예측값
pred = AM.predict(target_img_path)
print(pred)
