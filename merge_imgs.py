import cv2
import os
import numpy as np
import datetime

folder = "E:\\Portfolio\\TimeLapse\\src\\frame\\selected\\"

i=1

for filename in os.listdir(folder):
	print(os.path.join(folder,filename))
	if(i==1):
		image = cv2.imread(os.path.join(folder,filename))
	else:
		img = cv2.imread(os.path.join(folder,filename))
		#print(img)
		#print(image)
		image = np.minimum(image,img)
	i+=1

timestamp = datetime.datetime.now()
strtimestamp = timestamp.strftime("%m%d%Y%H%M%S")+'.jpg'
cv2.imwrite("sample\\"+strtimestamp,image)