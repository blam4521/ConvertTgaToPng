import os, sys
import os.path
from PIL import Image, ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES = True
import shutil



def convert_tga(img_dir):

	'''
	Takes a img_dir, copies the entire files in dir then looks through every orginal 
	image file extension tga and changes it according hardcoded input of a scale of 25%
	'''

	for aFile in os.listdir(img_dir):
		
		if aFile.endswith('tga'):
			
			img_file = Image.open(img_dir+"/"+aFile)
			
			width, height = (int(100 * img_file.size[0] / 100.0), 
													int(100 * img_file.size[1] / 100.0))

			print "resizing: ", aFile, " to width ", width, " x height ", height 
			img_file = img_file.resize((width, height), Image.ANTIALIAS)
			
			try:
				#logging.basicConfig()
				#fileName = os.path.splitext(aFile)[0] #without file extension
				
				img_file.save(img_dir+"/"+ aFile,format="tga", 
											optimize=True, 
											quality=100, 
											progressive=True)
				
				
			except IOError:
				print "exception saving file ", aFile
	
 

if __name__ == "__main__":
	f = open('test.txt','r')
	for line in f:
		img_dir = line.rstrip('\n')
		print "dealing with this directory:", img_dir
		convert_tga(img_dir);
		print "...saving done"


