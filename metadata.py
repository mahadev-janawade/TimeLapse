from PIL import Image
from PIL.ExifTags import TAGS

try:
	imgFile = Image.open('4.jpg')
	info = imgFile._getexif()
	if info:
		for (tag, value) in info.items():
			tagname = TAGS.get(tag, tag)
			print(tagname, value)
	else:
		print("None")


except:
	print("failed")