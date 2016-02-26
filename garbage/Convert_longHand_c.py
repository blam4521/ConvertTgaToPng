import os, sys
import os.path
from PIL import Image, ImageFile
import Tkinter, tkFileDialog
import shutil
import logging


def convert_tga(img_dir, scale_img):

	'''
	Takes a img_dir, copies the entire files in dir then looks through every orginal 
	image file extension tga and changes it according user input input scale
	'''
	#copy the original images into a backup directory
	large_subdir = img_dir + "/texture_large"
	'''
	if os.path.exists(large_subdir):
		print 'there is already a folder named %s'%(large_subdir)
	else:
		print 'folder not created, creating folder'
		makeDir = os.makedirs(large_subdir)
	'''
	print "copying originals into folder texture_large..."
	shutil.copytree(img_dir, large_subdir)
	print "...copying done"
	'''
	ext = ['png','jpg', 'vrimg', 'hdr','exr', 'tga', 'bmp', 'sgi','tif', 'vrst']

			for i in os.listdir(img_dir):
					if i.endswith(tuple(ext)):
						print i
						src_file = os.path.join(img_dir, i)
						dst_file = os.path.join(large_subdir, i)
						shutil.move(src_file, dst_file)
	'''
	for aFile in os.listdir(img_dir):
		
		if aFile.endswith('tga'):
			
			img_file = Image.open(img_dir+"/"+aFile).convert('RGB')
			
			width, height = (int(scale_img * img_file.size[0] / 100.0), 
													int(scale_img * img_file.size[1] / 100.0))

			print "resizing: ", aFile, " to width ", width, " x height ", height 
			img_file = img_file.resize((width, height), Image.ANTIALIAS)
			
			try:
				#logging.basicConfig()
				fileName = os.path.splitext(aFile)[0] #without file extension
				
				img_file.save(img_dir+"/"+ fileName +".tga",format="tga", 
											optimize=True, 
											quality=100, 
											progressive=True)
				os.remove(img_dir+"/"+aFile)
				
			except IOError:
				print "exception saving file ", aFile


#img_dir = "C:/Users/Bears/Downloads/Ant_Videos"
# root = Tkinter.Tk()
# root.withdraw() # remove main app window in background
# img_dir = tkFileDialog.askdirectory(parent=root,initialdir="C:/",title='Please select a directory')
# print "Selected directory: ", img_dir
#image_format = raw_input('Enter a file format: ')
#print image_format
scale_img = int(input('Enter a scale percent (0-100): '))
if scale_img == 100:
	print "scale of 100 has no effect, exiting program"
else: 
	f = open('blist.txt','r')
	for line in f:
		img_dir = line.rstrip('\n')
		print "dealing with this directory:", img_dir
		convert_tga(img_dir, scale_img);
		print "...conversion done"

		


