import cv2
import numpy as np
import copy
import time

def frameCount(inputLoc, i, val):
	success = True
	range = copy.deepcopy(val)
	while success:
		range += pow(10,i)
		frame = cv2.VideoCapture(inputLoc)
		frame.set(1,range)
		success, image = frame.read()
		frame.release()
		
	val = copy.deepcopy(range-pow(10,i))
	return val

def getFrameCount(inputLoc):
	start_time = time.time()
	frameNumber = 1
	frame = cv2.VideoCapture(inputLoc)
	frame.set(1,frameNumber)
	success, image = frame.read()

	range = 1

	i = range

	while success and i<11:	
		range = pow(10,i)
		frame = cv2.VideoCapture(inputLoc)
		frame.set(1,range)
		success, image = frame.read()
		frame.release()	
		i+=1
	i-=2

	val = 0

	while i!=-1:
		val = frameCount(inputLoc, i, val)
		i-=1
	print("%s"%(time.time() - start_time))
	return val

def main(inputLoc):
	count=getFrameCount(inputLoc)
	print(count)

if __name__=='__main__':
	inputLoc = '07142019212351.mp4'
	main(inputLoc)