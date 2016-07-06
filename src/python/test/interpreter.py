import os
import time
import threading


def listFiles():
	files = os.listdir(os.curdir)
	files = sorted(files)
	return files


def readFiles(files):
	for n in files:
		if(os.path.getctime(n) > time):   
			with open(n, 'r') as input:
				for line in input:
					if '..' in line:    #.. before this point is the header
						interpretFiles(n, input.tell())
		break	 #the files are sorted by timestamp, if the first file fail on the condition the others will also fail

	threading.Timer(5, readFiles, [listFiles()]).start()

def interpretFiles(n, pos):
	f = open(n, 'r')
	o = f.readline(pos)
	print o 

time = time.time()
files = listFiles()
readFiles(files)


