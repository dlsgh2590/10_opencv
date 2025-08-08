import cv2
import pytesseract
import numpy as np
import os

# 환경 변수 설정
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    # 1. 크기 조절 (필요하면)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # 2. 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 3. 노이즈 제거 및 임계처리
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def extract_text(img):
    # lang 설정은 필요에 따라 조정 (한국어, 영어 등)
    text = pytesseract.image_to_string(img, lang='eng')
    return text.strip()

if __name__ == "__main__":
    img_path = 'traffic_sign.jpg'  # 교통표지판 사진 경로
    preprocessed_img = preprocess_image(img_path)
    text = extract_text(preprocessed_img)
    print("인식된 텍스트:", text)

    # 결과 확인용 이미지 출력
    cv2.imshow('Preprocessed', preprocessed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()