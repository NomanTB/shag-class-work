import cv2
from  PIL import Image

image_path = 'cat.jpeg'

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image =cv2.imread(image_path)

cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('glasses.png')

cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')
for (x,y,w,h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)),glasses)
    cat.save('cat_ochki.png')
    cat_ochki = cv2.imread('cat_ochki.png')
    cv2.imshow('Cat_ochki', cat_ochki)
    cv2.waitKey()