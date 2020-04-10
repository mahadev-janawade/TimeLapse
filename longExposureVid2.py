import cv2
import os
import numpy as np
import datetime
import FrameCount

(rAvg, gAvg, bAvg) = (None, None, None)
total = 0


i=1

image_loc = "input/2.mp4"
totalCount = FrameCount.getFrameCount(image_loc)


print(totalCount)
frame_no = int(input('Enter start frame no: '))
end_limit = int(input('Enter end frame no: '))

jump = int(input('Enter frame jump no: '))


for index1 in range(frame_no,end_limit,jump):
	input1 = cv2.VideoCapture(image_loc)
	input1.set(i, index1)
	success,frame = input1.read()

	(B, G, R) = cv2.split(frame.astype("float"))
	if rAvg is None:
		rAvg = R
		bAvg = B
		gAvg = G
 
	# otherwise, compute the weighted average between the history of
	# frames and the current frames
	else:
		rAvg = ((total * rAvg) + (1 * R)) / (total + 1.0)
		print(rAvg)
		print(R)
		print("---------------------------------------")
		gAvg = ((total * gAvg) + (1 * G)) / (total + 1.0)
		bAvg = ((total * bAvg) + (1 * B)) / (total + 1.0)
 
	# increment the total number of frames read thus far
	total+=1
	input1.release()
	
	image = cv2.merge([bAvg, gAvg, rAvg]).astype("uint8")
	timestamp = datetime.datetime.now()
	strtimestamp = "frame/"+timestamp.strftime("%m%d%Y%H%M%S")+'.jpg'
	cv2.imwrite(strtimestamp,image)