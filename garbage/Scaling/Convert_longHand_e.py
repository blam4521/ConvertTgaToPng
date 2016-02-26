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
	dest = img_dir + "/textures_small"
	src = img_dir + "/textures"
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
	

	'''
	for aFile in os.listdir(img_dir):
		
		if aFile.endswith('tga'):
			
			img_file = Image.open(img_dir+"/"+aFile)
			
			width, height = (int(25 * img_file.size[0] / 100.0), 
													int(25 * img_file.size[1] / 100.0))

			print "resizing: ", aFile, " to width ", width, " x height ", height 
			img_file = img_file.resize((width, height), Image.ANTIALIAS)
			
			try:
				#logging.basicConfig()
				#fileName = os.path.splitext(aFile)[0] #without file extension
				
				img_file.save(img_dir+"/"+ aFile,format="tga", 
											optimize=True, 
											quality=100, 
											progressive=True)
				#os.remove(img_dir+"/"+aFile)
				
			except IOError:
				print "exception saving file ", aFile
	'''
 

if __name__ == "__main__":
	f = open('test.txt','r')
	for line in f:
		img_dir = line.rstrip('\n')
		print "dealing with this directory:", img_dir
		convert_tga(img_dir);
		print "...saving done"


