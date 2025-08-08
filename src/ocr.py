import easyocr
import cv2
import matplotlib.pyplot as plt

#reader = easyocr.Reader(['ch_tra','en'])
reader = easyocr.Reader(['ko','en'])
#img_path = '../img/chinese_tra.jpg'
img_path = '../img/abc.png'
#result = reader.readtext('chinese_tra.jpg')

img = cv2.imread(img_path)

#plt.figure(figsize=(8, 8))
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

# 이미지 텍스트 인식
#result = reader.readtext(img_path)

# rotation_info로 세로 텍스트 인식 강화
result = reader.readtext(img_path, rotation_info=[90, 270])
print(result)

# 인식된 텍스트 확인해보기
THRESHOLD = 0.5

for bbox, text, conf in result:
    if conf >= THRESHOLD:
        print(text)
        cv2.rectangle(img, pt1=bbox[0], pt2=bbox[2], color=[0, 255, 0], thickness=2)
    plt.figure(figsize=(8,8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()