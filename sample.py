a = 0
b = 0
c = 0
d = 0

for a in range(0,20):
	for adec in range(0,10):
		for b in range(0,20):
			for bdec in range(0,10):
				for c in range(0,20):
					for cdec in range(0,10):
						for d in range(0,20):
							for ddec in range(0,10):
								if((float(a)+float('0.'+str(adec)))+(float(b)+float('0.'+str(bdec))) == 8.0 and (float(c)+float('0.'+str(cdec)))-(float(d)+float('0.'+str(ddec))) ==6.0 and (float(a)+float('0.'+str(adec)))+(float(c)+float('0.'+str(cdec)))==13.0 and (float(b)+float('0.'+str(bdec)))+(float(d)+float('0.'+str(ddec)))==8.0):
									print((float(a)+float('0.'+str(adec))))
									print((float(b)+float('0.'+str(bdec))))
									print((float(c)+float('0.'+str(cdec))))
									print((float(d)+float('0.'+str(ddec))))