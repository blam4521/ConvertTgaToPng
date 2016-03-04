import os, sys
import os.path
from PIL import Image, ImageFile
import shutil



def convert_tga(img_dir):

	'''
	Takes a img_dir, copies the entire files in dir then looks through every orginal 
	image file extension tga and changes it according hardcoded input of a scale of 25%
	'''

	#copy the original images into a backup directory
	dest = img_dir + " "
	src = img_dir + " "
	#checks to see if there is a directory, boolean logic, not true = false, not false = true
	
	
	if not os.path.exists(dest):
		#make = os.makedirs(dest)
		print "Making dir: ", dest
		
		for image in os.listdir(src):
			print image
		print "copying originals into folder textures_small..."
		shutil.copytree(src, dest)
		#print os.listdir(dest)
		print "...copying done"
	
	try:
		if not len(os.listdir(src)) == len(os.listdir(dest)):
			print "ERROR, dest does not match src"
		else:
			print "DES AND SRC MATCHES"
	
	#try and except hard stop on the entire function 
	except:
		print "ERROR: Comparing length of Src and Dest"
	

	
 

if __name__ == "__main__":
	f = open(' ','r')
	for line in f:
		img_dir = line.rstrip('\n')
		print "dealing with this directory:", img_dir
		convert_tga(img_dir);
		print "...saving done"


