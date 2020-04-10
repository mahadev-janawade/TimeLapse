import numpy as np
import cv2
import os
import datetime
import FrameCount
from matplotlib import pyplot as plt

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
	
	@staticmethod
	def squareImage(frame,height=0,width=0):
		if(frame.shape[0]>frame.shape[1]):
			if(height>0 and width>0):
				frame1 = np.zeros(shape=[height,width,3],dtype=np.uint8)
				frame1[:,:] = [255,255,255]
				print(frame1.shape[0])
				print(frame1.shape[1])
				if((frame1.shape[0] - frame.shape[0])%2==0):
					pad = (int)((frame1.shape[0] - frame.shape[1])/2)
					frame1[:,pad:frame1.shape[1]-pad] = frame
					return frame1
				else:
					pad = (int)((frame1.shape[0] - frame.shape[1])/2)
					frame1[:,pad+1:frame1.shape[1]-pad] = frame
					return frame1
					
				
			else:
				frame1 = np.zeros(shape=[frame.shape[0],frame.shape[0],3],dtype=np.uint8)
				frame1[:,:] = [255,255,255]
				print(frame1.shape[0])
				print(frame1.shape[1])
				if((frame1.shape[0] - frame.shape[0])%2==0):
					pad = (int)((frame1.shape[0] - frame.shape[1])/2)
					frame1[:,pad:frame1.shape[1]-pad] = frame
					return frame1
				else:
					pad = (int)((frame1.shape[0] - frame.shape[1])/2)
					frame1[:,pad+1:frame1.shape[1]-pad] = frame
					return frame1
			
			
		elif(frame.shape[1]>frame.shape[0]):
			if(height>0 and width>0):
				print(frame.shape[0])
				print(frame.shape[1])
				frame1 = np.zeros(shape=[height,width,3],dtype=np.uint8)
				frame1[:,:] = [255,255,255]
				print(frame1.shape[0])
				print(frame1.shape[1])
				if((frame1.shape[0] - frame.shape[0])%2==0):
					pad = (int)((frame1.shape[0] - frame.shape[0])/2)
					frame1[pad:frame1.shape[0]-pad,:] = frame
					return frame1
				
				else:
					pad = (int)((frame1.shape[0] - frame.shape[0])/2)
					frame1[pad+1:frame1.shape[0]-pad,:] = frame
					return frame1
				
			else:
				frame1 = np.zeros(shape=[frame.shape[1],frame.shape[1],3],dtype=np.uint8)
				frame1[:,:] = [255,255,255]
				print(frame1.shape[0])
				print(frame1.shape[1])
				if((frame1.shape[0] - frame.shape[0])%2==0):	
					pad = (int)((frame1.shape[0] - frame.shape[0])/2)
					frame1[pad:frame1.shape[0]-pad,:] = frame
					return frame1
				else:
					pad = (int)((frame1.shape[0] - frame.shape[0])/2)
					frame1[pad+1:frame1.shape[0]-pad,:] = frame
					return frame1
			
		else:
			return frame
		
		
	
	@staticmethod
	def changeRGB(blue, green, red,image):
		addElement = [blue,green,red]
		addElement1 = np.array(addElement)
		image1 = np.add(image,addElement1)
		image1[image1>255]=255
		image1[image1<0] = 0
		img8 = image1.astype('uint8')
		return img8
	
	@staticmethod
	def rotateImage(image,degrees):
		a = int(degrees/90)
		for i in range(a):
			image = np.rot90(image)
		return image
	
	
	def timelapse(self, totalFrameCount,image_Location):
		print(totalFrameCount)
		start = 0
		end = totalFrameCount
		self.selectFrames = input('Enter frame select: ')
		#self.fourcc = cv2.VideoWriter_fourcc(*self.codec)
		self.fps = int(self.fps)
		timestamp = datetime.datetime.now()
		strtimestamp = "output/" + timestamp.strftime("%m%d%Y%H%M%S")+'.mp4'
		fourc = cv2.VideoWriter_fourcc(*'mp4v')
		out = cv2.VideoWriter(strtimestamp,fourc, self.fps, (1920,1080))
		frame_no = start
		inc = int(self.selectFrames)
		success = True
		i=1
		j=1
		fpscount = 0
		#self.preview()
		print("Processing..... Please wait....")
		cap = cv2.VideoCapture(image_Location)
		cap.set(i, frame_no)
		success, image = cap.read()
		frame1 = totalFrameCount*1/100
		frame2 = totalFrameCount*30/100
		frame3 = totalFrameCount*30/100
		frame4 = totalFrameCount*60/100
		frame5 = totalFrameCount*60/100
		frame6 = totalFrameCount*80/100		
		while(success and frame_no<end):
			if(frame_no >= frame1 and frame_no <= frame2):
				#increment = inc
				increment = inc*80/100
			elif(frame_no >= frame3 and frame_no <= frame4):
				#increment = inc
				increment = inc*60/100
			elif(frame_no >= frame5 and frame_no <= frame6):
				#increment = inc
				increment = inc*40/100
			else:
				#increment = inc
				increment = inc*30/100
			
			#image = videoEdit.changeRGB(10,0,-10,image)
			
			#image = videoEdit.rotateImage(image,180)
			#cv2.imshow("dfs",image)
			#cv2.waitKey(100)
			out.write(image)
			
			fpscount += 1
			frame_no += increment 
			cap.release()
			cap = cv2.VideoCapture(image_Location)
			cap.set(i, frame_no)
			success, image = cap.read()
			j = j+1
		print("TimeLapse created!!")
		out.release()

	
	def combine(self):
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		#fourcc = cv2.VideoWriter_fourcc(*'h264')
		#out = cv2.VideoWriter('output/output.mp4',fourcc, 20, (1820,980))
		out = cv2.VideoWriter('output/timeLapseCombine.mp4',fourcc, 20, (1920,1080))
		cap = cv2.VideoCapture('7.mp4')
		success, frame = cap.read()
		while(success):
			out.write(frame)
			success, frame = cap.read()
	
		cap.release()
	
		cap = cv2.VideoCapture('8.mp4')
		success, frame = cap.read()
		while(success):
			out.write(frame)
			success, frame = cap.read()
		cap.release()
	
	def square(self, imageLoc,rotate=False,rotateDir=0):
		framecount = 1
		jumpcount = 1
		input1 = cv2.VideoCapture(imageLoc)
		input1.set(1,framecount)
		success,frame = input1.read()
		size = 0
		if(frame.shape[0]>frame.shape[1]):
			size = frame.shape[0]
		elif(frame.shape[0] <= frame.shape[1]):
			size = frame.shape[1]
		
		timestamp = datetime.datetime.now()
		strtimestamp = "sqaure/" + timestamp.strftime("%m%d%Y%H%M%S")+'.mp4'
		
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		out = cv2.VideoWriter(strtimestamp,fourcc, 25, (size,size))
		
		input1.set(1,framecount)
		success,frame = input1.read()
		count = 0
		
		while success:
			print(framecount)
			frame = videoEdit.squareImage(frame,size,size)
			if(rotate == True):
				frame = videoEdit.rotateImage(frame,rotateDir)
			out.write(frame)
			count+=1
			input1.release()
			framecount +=  jumpcount
			input1 = cv2.VideoCapture(imageLoc)
			input1.set(1,framecount)
			success,frame = input1.read()
	
	def frameExtract(self):
		framecount = 1
		jumpcount = 1
		self.inputLoc = input('Enter Input file:')
		input1 = cv2.VideoCapture(self.inputLoc)
		self.outputLoc = input('Enter Output Location:')
		input1.set(1,framecount)
		success,frame = input1.read()
		count = 0
		while success:
			cv2.imwrite("sample/frame_%d.jpg"%(count), frame)
			count+=1
			input1.release()
			framecount +=  jumpcount
			input1 = cv2.VideoCapture(self.inputLoc)
			input1.set(1,framecount)
			success,frame = input1.read()
	
	def image2Video(self):
		self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		out = cv2.VideoWriter(self.outputLocation,self.fourcc,int(self.fps), (1920,1080))
		for filename in os.listdir(self.videoLocation):
			img = cv2.imread(os.path.join(self.videoLocation,filename))
			out.write(img)
	

	def resizeImage(self,image):
		frame = cv2.imread(image)
		resizeimg = cv2.resize(frame,None,fx=3,fy=4)
		cv2.imwrite('zimage1.jpg',resizeimg)

	def compareImg(self,img1,img2):
		imgRead1 = cv2.imread(img1)
		imgRead2 = cv2.imread(img2)
		for i in range(100,120):
			print(imgRead1[i,100],end=" ")
			print(imgRead2[i,100])
		
	def sharpenImage(self,img1):
		imgRead1 = cv2.imread(img1)
		kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]], np.float32)
		kernel=1/3*kernel
		sharpened = cv2.filter2D(imgRead1, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
		cv2.imwrite('dsa.jpg',sharpened)

	
	def normalizeImage(self, img1):
		img = cv2.imread(img1)
		img = cv2.resize(img, (800, 800))
		norm_image = cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)	
		cv2.imwrite('qwe.jpg',norm_image)

	def increase_brightness(self,img, value=30):
    		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    		h, s, v = cv2.split(hsv)
    		lim = 255 - value
    		v[v > lim] = 255
    		v[v <= lim] += value
    		final_hsv = cv2.merge((h, s, v))
    		img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    		cv2.imwrite('qwe1.jpg',img)

	def edit(self,totalCount,image_Location):
		input = cv2.VideoCapture(image_Location)
		input.set(1, max)
		success, frame = input.read()
		size = frame.shape
		height = size[0]
		width = size[1]
		x0y0 = 0
		xny0 = 0
		x0yn = 0
		xnyn = 0
		i=1
		print(height)
		print(width)
		timestamp = datetime.datetime.now()
		strtimestamp = timestamp.strftime("%m%d%Y%H%M%S")+'.mp4'
		fourc = cv2.VideoWriter_fourcc(*'mp4v')
		out = cv2.VideoWriter(strtimestamp,fourc, 20, (1920,1080))
		n=60

		i1 = x0y0
		i2 = xny0
		i3 = x0yn
		i4 = xnyn
		while success:
			if(i<n):
				x0y0 = 0.5
				xny0 = 0.25
				x0yn = 0.5
				xnyn = 2.0
			elif(i>=n):
				x0y0 = 0.5
				xny0 = 0.0
				x0yn = 1
				xnyn = 0.2
			i1 += x0y0
			i2 += xny0
			i3 += x0yn
			i4 += xnyn	
			frame1 = frame[int(i1):(height-int(i2)), int(i3):(width-int(i4))]
			i+=1
			resizeimg = cv2.resize(frame1,(1920,1080),interpolation = cv2.INTER_LINEAR)
			#resizeimg = videoEdit.changeRGB(10,0,-10,resizeimg)
			out.write(resizeimg)
			
			success, frame = input.read()
		out.release()
		input.release()
		

	def edit1(self,totalCount,image_Location):
		max = 1
		start = 40
		input = cv2.VideoCapture(image_Location)
		input.set(1, start)
		success, frame = input.read()
		size = frame.shape
		height = size[0]
		width = size[1]
		i=1
		print(height)
		print(width)
		timestamp = datetime.datetime.now()
		strtimestamp = timestamp.strftime("%m%d%Y%H%M%S")+'.mp4'
		fourc = cv2.VideoWriter_fourcc(*'mp4v')
		out = cv2.VideoWriter(strtimestamp,fourc, 25, (1920,1080))
		n=2000

		while success:
			if(i<n):
				x0y0 = 0.5
				xny0 = 0.1
				x0yn = 0.5
				xnyn = 0.5
			elif(i>=n):
				x0y0 = 0.5
				xny0 = 0.0
				x0yn = 1
				xnyn = 0.2
			print(max)
			i1 = max * x0y0
			i2 = max * xny0
			i3 = max * x0yn
			i4 = max * xnyn	
			frame1 = frame[int(i1):(height-int(i2)), int(i3):(width-int(i4))]
			i+=1
			resizeimg = cv2.resize(frame1,(1920,1080),interpolation = cv2.INTER_LINEAR)
			#resizeimg = videoEdit.changeRGB(10,0,-10,resizeimg)
			out.write(resizeimg)
			input.release()
			start += 1
			input = cv2.VideoCapture(image_Location)
			input.set(1, start)
			max += 1
			success, frame = input.read()
		out.release()
		input.release()

	@staticmethod
	def threshold(image):
		#frame = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
		frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		ret,img = cv2.threshold(frame,125,255,cv2.THRESH_BINARY)
		
		#cv2.imwrite('sample.jpg',img)
		#img = cv2.imread('sample.jpg')
		
		
		#image[frame1>0] = 255
		#black=np.where((img[:,:,0]<=20) & (img[:,:,1]<=20) & (img[:,:,2]<=20))
		#white=np.where((img[:,:,0]>20) & (img[:,:,1]>20) & (img[:,:,2]>20))

		#Turn black pixels to white and vice versa
		#img[black]=(0,0,0)
		#img[white]=(255,255,255)
		#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return img	
	

	@staticmethod
	def foregroundExtract(img):
		mask = np.zeros(img.shape[:2],np.uint8)

		bgdModel = np.zeros((1,65),np.float64)
		fgdModel = np.zeros((1,65),np.float64)

		rect = (50,50,4000,2000)
		cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

		mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
		img = img*mask2[:,:,np.newaxis]
		return img

	
		
def main():
	choice = input('1-> combine videos, 2-> timelapse, 3->extract all frames,4->Images to Video, 5->Image Resize, 10-> Resize')
	if(choice=='1'):
		image_Location = 'output/04042020225241.mp4'
		totalCount = FrameCount.getFrameCount(image_Location)
		v1 = videoEdit()
		v1.combine()
		
	elif(choice=='2'):
		image_Location = 'input/cloud_lapse.mp4'
		totalCount = FrameCount.getFrameCount(image_Location)
		v = videoEdit()
		v.initialize()	
		v.timelapse(totalCount,image_Location)
		
	elif(choice=='3'):
		image_Location = 'output/04042020225241.mp4'
		totalCount = FrameCount.getFrameCount(image_Location)
		frame = videoEdit()
		frame.frameExtract()
	
	elif(choice =='4'):
		image_Location = 'output/04042020225241.mp4'
		totalCount = FrameCount.getFrameCount(image_Location)
		imgVid = videoEdit()
		imgVid.initialize()
		imgVid.image2Video()

	elif(choice =='5'):
		imgResize = videoEdit()
		imgResize.resizeImage('\\merge1\\a\\zIMG_20191022_190152630.jpg')

	elif(choice =='6'):
		imgCmp = videoEdit()
		imgCmp.compareImg('image1.jpg','image1 (2).jpg')	

	elif(choice == '7'):
		sharpen = videoEdit()
		sharpen.sharpenImage('merge1400.jpg')

	elif(choice == '8'):
		norm = videoEdit()
		norm.normalizeImage('merge100.jpg')

	elif(choice == '9'):
		brightness = videoEdit()
		img = cv2.imread('qwe.jpg')
		brightness.increase_brightness(img,-10)
	
	elif(choice == '10'):
		image_Location = 'output/04042020225241.mp4'
		totalCount = FrameCount.getFrameCount(image_Location)
		resizeVideo = videoEdit()
		resizeVideo.edit(totalCount,image_Location)

	elif(choice == '11'):
		image_Location = 'input/timelapse_today.mp4'
		totalCount = FrameCount.getFrameCount(image_Location)
		resizeVideo1 = videoEdit()
		resizeVideo1.edit1(totalCount,image_Location)

	elif(choice == '12'):
		frame = cv2.imread('input/IMG_20191214_143629713_HDR-07.jpeg')
		#print(frame)
		frame1 = videoEdit.squareImage(frame)
		cv2.imwrite("sqaure/mannavanur3.png",frame1)
		
	elif(choice == '13'):
		frame = cv2.imread('H:/kodaikanal/IMG_20191214_144831145_HDR.jpg')
		#print(frame)
		frame1 = videoEdit.threshold(frame)
		cv2.imwrite('6565611.png',frame1)
		
	elif(choice == '14'):
		frame = cv2.imread('H:/kodaikanal/IMG_20191214_144831145_HDR.jpg')
		#print(frame)
		frame1 = videoEdit.foregroundExtract(frame)
		cv2.imwrite('6foreground.png',frame1)	
		
	elif(choice == '15'):
		image_Location = '04072020165853.mp4'
		rotate = False
		totalCount = FrameCount.getFrameCount(image_Location)
		print(totalCount)
		resizeVideo1 = videoEdit()
		#image location, rotate images? , rotate degree. 
		resizeVideo1.square(image_Location,rotate,270)
		
	else:
		print("Invalid Input")


if __name__ == '__main__':
	main()
