import numpy as np
import cv2

class videoEdit:
	def __init__(self):
		self.mp4List = ['h264','mp4v']
		self.aviList = ['I420','PIM1','MJPG','DIV3','DIVX','U263','I263','FLV1']
	def test(self):
		print(self.a)
	

	def initialize(self):
		self.videoLocation = input("Enter video name:")
		self.outputLocation = input("Output filename: ")
		self.fps = input("Enter Frames Per second:")
		if(self.outputLocation.endswith('.mp4')):
			print('Available Codec List for MP4 file\n1-> h264,\n2-> mp4v')
			codecChoice = input('\nSelect 1 codec: ')
			self.codec = self.mp4List[int(codecChoice)-1]
		
		elif(self.outputLocation.endswith('.avi')):
			print('Available Codec List for MP4 file\n1-> I420,\n2-> PIM1,\n3-> MJPG,\n4-> DIV3,\n5-> DIVX,\n6-> U263,\n7-> I263,\n8-> FLV1')
			codecChoice = input('\nSelect 1 codec: ')
			self.codec = self.aviList[int(codecChoice)-1]
	
	
	def preview(self):
		frame_no = 1
		inc = int(self.selectFrames)
		i=1
		fpscount = 0
		cap = cv2.VideoCapture('input/6.mp4')
		cap.set(i, frame_no)
		success, frame = cap.read()
		print(frame.shape)
		print(frame)
		image = cv2.resize(frame,(400,300),interpolation = cv2.INTER_AREA)
		print(image.shape)
		cv2.waitKey(1000)
		while(success):
			cv2.imshow("frame",image)
			cap = cv2.VideoCapture('input/6.mp4')
			cap.set(i, frame_no)
			success, image = cap.read()
			fpscount += 1
			frame_no += inc
			image = cv2.resize(image,(400,300),interpolation = cv2.INTER_AREA)
			cap.release()
	
	def timelapse(self):
		self.selectFrames = input('Enter frame select: ')
		self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
		self.fps = int(self.fps)
		out = cv2.VideoWriter(self.outputLocation,self.fourcc, self.fps, (1920,1080))
		frame_no = 1
		inc = int(self.selectFrames)
		success = True
		i=1
		fpscount = 0
		self.preview()
		print("Processing..... Please wait....")
		while(success):
			cap = cv2.VideoCapture('input/6.mp4')
			cap.set(i, frame_no)
			success, image = cap.read()
			out.write(image)
			fpscount += 1
			frame_no += inc
			cap.release()
		print("TimeLapse created!!")
		out.release()

	
	def combine(self):
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		#fourcc = cv2.VideoWriter_fourcc(*'h264')
		#out = cv2.VideoWriter('output/output.mp4',fourcc, 20, (1820,980))
		out = cv2.VideoWriter('output/output.mp4',fourcc, 20, (1920,1080))
		cap = cv2.VideoCapture('sunrise1.mp4')
		success, frame = cap.read()
		while(success):
			out.write(frame)
			success, frame = cap.read()
	
		cap.release()
	
		cap = cv2.VideoCapture('sunrise2.mp4')
		success, frame = cap.read()
		image = frame
		image1 = np.zeros((1080,1920,3), np.uint8)
		image1[:,:] = (0,0,0)
		image1[:,50:1870] = image
		while(success):
			out.write(image1)
			success, image = cap.read()
			image1 = np.zeros((1080,1920,3), np.uint8)
			image1[:,:] = (0,0,0)
			image1[:,50:1870] = image;
		
		cap.release()
	
	def frameExtract(self):
		self.inputLoc = input('Enter Input file:')
		input1 = cv2.VideoCapture(self.inputLoc)
		self.outputLoc = input('Enter Output Location:')
		success,frame = input1.read()
		count = 0
		while success:
			cv2.imwrite("%s/frame_%d.jpg"%(self.outputLoc,count), frame)
			count+=1
			success,frame = input1.read()
	

def main():
	choice = input('1-> combine videos, 2-> timelapse, 3->extract all frames')
	if(choice=='1'):
		v1 = videoEdit()
		v1.combine()
		
	elif(choice=='2'):
		v = videoEdit()
		v.initialize()	
		v.timelapse()
		
	elif(choice=='3'):
		frame = videoEdit()
		frame.frameExtract()
		
		
	elif(choice=='4'):
		vE = videoEdit()
		vE.a = 10
		vE.b = 19
		vE.test()
	
	
	else:
		print("Invalid Input")


if __name__ == '__main__':
	main()
