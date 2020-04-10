import cv2
import os
import glob
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('output.mp4',fourcc, 10.0, (1920,1080))
img_dir = "pics" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
	print(f1)
	img = cv2.imread(f1)
	resizeImage = cv2.resize(img,(1920,1080))
	out.write(resizeImage)
out.release()