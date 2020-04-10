import cv2
import numpy as np

im= cv2.VideoCapture("wqeqw.mp4")
success, frame = im.read()
while success:
	frame = cv2.resize(frame,(480,360))
	cv2.imshow("fdd",frame)
	cv2.waitKey(100)
	success, frame = im.read()