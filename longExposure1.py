import cv2
import os
import numpy as np
import datetime

(rAvg, gAvg, bAvg) = (None, None, None)
total = 0

folder = "H:\\C Driver\\Desktop\\sfd\\TimeLapse\\src\\frames2\\"

i=1

for filename in os.listdir(folder):
	print(os.path.join(folder,filename))
	frame = cv2.imread(os.path.join(folder,filename))
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

	
image = cv2.merge([bAvg, gAvg, rAvg]).astype("uint8")
timestamp = datetime.datetime.now()
strtimestamp = timestamp.strftime("%m%d%Y%H%M%S")+'.jpg'
cv2.imwrite("crackers\\"+strtimestamp,image)