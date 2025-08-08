import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(['ch_tra', 'en'])
img_path = '../img/chinese_tra.jpg'
#result = reader.readtext('chinese_tra.jpg')

img = cv2.imread(img_path)

plt.figure(figsize=(8, 8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show() 