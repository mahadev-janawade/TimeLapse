import cv2
import numpy as np
import imutils
import FrameCount

def imageMerge(inputLoc,start,end):
	frame2 = cv2.VideoCapture(inputLoc)
	i=0
	frame2.set(1,start+i)
	success, image = frame2.read()
	success, img1 = frame2.read()
	while success and (start+i)<end:
		image = np.minimum(image,img1)
		frame2.release()
		i+=1
		frame2 = cv2.VideoCapture(inputLoc)
		frame2.set(1,start+i)
		success, img1 = frame2.read()
	frame2.release()
	
	#rotate_image = imutils.rotate(image,180)
	cv2.imwrite('merge1/merge%d.jpg'%(start+i),image)
	return image


inputLoc = 'output/03262020193212.mp4'

frame = cv2.VideoCapture(inputLoc)
success = True
count = 0
i = 112

numberOfFrames = FrameCount.getFrameCount(inputLoc)

startFrame = 0
frameCountToMerge = 50
frameJumpCount = 50

while success:
	try:
		count +=1	
		
		frame1 = cv2.VideoCapture(inputLoc)
		frame1.set(1,startFrame)
		success1, im1 = frame1.read()
		 
		frame2 = cv2.VideoCapture(inputLoc)
		frame2.set(1,startFrame+frameCountToMerge)
		success2, im2 = frame2.read()
		
		frame1.release()
		frame2.release()
		
		if success1 and success2:
			img1 = imageMerge( inputLoc , startFrame , startFrame+frameCountToMerge )
			success = True
		
		elif success1 and success2==False:
			findLastFrame = startFrame
			successImage = True
			
			while successImage:
				frame1 = cv2.VideoCapture(inputLoc)
				frame1.set(1,findLastFrame)
				successImage, img1 = frame.read()
				findLastFrame += 1
				frame1.release()
			
			img1 = imageMerge( inputLoc , startFrame , findLastFrame-1 )
			success= False
		else:
			success = False
		print(success)
		startFrame += frameJumpCount

	except:
		success=False

#rotate_image = imutils.rotate(img1,180)
cv2.imwrite('merge1/hello%d.jpg'%i,img1)