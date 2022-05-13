import glob
import CaptchaCracker as cc

# 학습 이미지 데이터 경로
train_img_path_list = glob.glob("interpark/*.png")

# 학습 이미지 데이터 크기
img_width = 150
img_height = 40

# 모델 생성 인스턴스
CM = cc.CreateModel(train_img_path_list, img_width, img_height)

# 모델 학습
model = CM.train_model(epochs=100)

# 모델이 학습한 가중치 파일로 저장
model.save_weights("model/weights2.h5")