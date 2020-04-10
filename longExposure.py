import imutils
import cv2

(rAvg, gAvg, bAvg) = (None, None, None)
total = 0
 
# open a pointer to the video file
stream = cv2.VideoCapture("input/41.mp4")

while True:
	# grab the frame from the file stream
	(grabbed, frame) = stream.read()
 
	# if the frame was not grabbed, then we have reached the end of
	# the sfile
	if not grabbed:
		break
 
	# otherwise, split the frmae into its respective channels
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

avg = cv2.merge([bAvg, gAvg, rAvg]).astype("uint8")
cv2.imwrite("fqwe.jpg", avg)
 
# do a bit of cleanup on the file pointer
stream.release()