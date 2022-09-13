# Telegram-bot-text-extractor
This bot use Open-CV and EasyOCR libraries to extract highlighted text from images sent in a chat group

## Input example:

![example1](https://user-images.githubusercontent.com/71794972/190015812-31f142d6-4520-4ce6-b153-d45d5c4eb57a.jpg)

## Firts we try to find the contours in the image 
![image](https://user-images.githubusercontent.com/71794972/190015910-c624ede5-76c4-4406-a360-f3e97a05d330.png)
## Then we extract only the contours we need
![image](https://user-images.githubusercontent.com/71794972/190016073-8dffa6ff-dd0f-4ddd-94a5-55c7279f4475.png)
## After that we pass this image to easyocr library to extract the text.
