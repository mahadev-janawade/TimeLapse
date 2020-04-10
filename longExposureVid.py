import cv2
import os
import numpy as np
import datetime
import FrameCount

(rAvg, gAvg, bAvg) = (None, None, None)
total = 0


i=1

image_loc = "input/mmmmmmmmmmmmm.mp4"
totalCount = FrameCount.getFrameCount(image_loc)


print(totalCount)
frame_no = int(input('Enter start frame no: '))
end_limit = int(input('Enter end frame no: '))

jump = int(input('Enter frame jump no: '))

input1 = cv2.VideoCapture(image_loc)
input1.set(i, frame_no)
success,frame = input1.read()

total = 0

while success and frame_no<end_limit:
	(B, G, R) = cv2.split(frame.astype("float"))
	if rAvg is None:
		rAvg = R
		bAvg = B
		gAvg = G
 
	# otherwise, compute the weighted average between the history of
	# frames and the current frames
	else:
		rAvg = ((total * rAvg) + (1 * R)) / (total + 1.0)
		gAvg = ((total * gAvg) + (1 * G)) / (total + 1.0)
		bAvg = ((total * bAvg) + (1 * B)) / (total + 1.0)
 
	# increment the total number of frames read thus far
	total += 1
	print(total)
	input1.release()
	input1 = cv2.VideoCapture(image_loc)
	frame_no += jump
	input1.set(i, frame_no)
	success,frame = input1.read()
	
image = cv2.merge([bAvg, gAvg, rAvg]).astype("uint8")
timestamp = datetime.datetime.now()
strtimestamp = timestamp.strftime("%m%d%Y%H%M%S")+'.jpg'
cv2.imwrite(strtimestamp,image)