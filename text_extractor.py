import cv2
import numpy as np
import easyocr
import csv

COINS = []
with open('coins.txt','r') as coins_txt:
    for line in coins_txt:
        x = line[:-1]
        COINS.append(x)
    coins_txt.close()

def get_text(path):
    img = cv2.imread(path)
    blurred_img = cv2.GaussianBlur(img, (5,5),0)
    hsv = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)
    lower_color = np.array([20, 20, 20])
    upper_color = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # getting the contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    stencil = np.zeros(img.shape).astype(img.dtype)
    
    # finding the highlight in the contours
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(img, contour, -1, (255, 0 , 0), 3)
            cv2.fillPoly(stencil,[contour],(255,255,255))
    
    # blocking everything exept the highlighted text
    result = cv2.bitwise_and(img, stencil)

    # reading from the image
    reader = easyocr.Reader(['en'], gpu=True)
    reader_results = reader.readtext(result)
    text = ''
    global COINS
    if len(reader_results)==1:
        text = reader_results[0][1]
    elif len(reader_results) == 0:
        reader_results = reader.readtext(img)
        if len(reader_results)==1:
            text = reader_results[0][1]
    if "IUSDT" in text:
            text = text[:-5]
    if text in COINS:
        return text
    elif text.isalpha():
        COINS.append(text)
        print(f"The new coin {text} was found, adding it to the coins now")
        with open("coins.txt","a") as file:
            file.write(f"{text}\n")
            file.close()
        print("done")
        return text
    else:
        return "No related coins detected"
