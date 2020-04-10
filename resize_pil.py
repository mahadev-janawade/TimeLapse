from PIL import Image
import cv2
import numpy as np

img = Image.open("zIMG_20191022_190152630.jpg")
img = img.resize((1920,1080),Image.ANTIALIAS)
img.save("dsasad.jpg")

im= cv2.imread("zIMG_20191022_190152630.jpg")
im1 = cv2.resize(im,(23040,10000))
im2 = cv2.resize(im1,(480,360))
cv2.imshow("fdd",im2)
cv2.waitKey(0)
cv2.imwrite("fsdsdf.jpg",im1)