import os, sys
import os.path
from PIL import Image, ImageFile
import Tkinter, tkFileDialog
import shutil


def convert_jpg(img_dir, image_format, scale_img):

	'''
	Takes a img_dir, looks through every image file extension set by the users and changes it according to their
	input scale
	'''
	subdirectory = img_dir + "/texture_small"
	
	if os.path.exists(subdirectory):
		print 'there is already a folder named %s'%(subdirectory)
		
	else:
		print 'folder not created, creating folder'
		makeDir = os.makedirs(subdirectory)

	

	for aFile in os.listdir(img_dir):
		#print aFile
		if aFile.endswith(image_format):
			#print "this is a jpg"
			img_file = Image.open(img_dir+"/"+aFile).convert('RGB')
			#print "img file: ", img_file
			width, height = (int(scale_img * img_file.size[0] / 100.0), 
													int(scale_img * img_file.size[1] / 100.0))

			print "resizing: ", aFile, " to width ", width, " x height ", height 
			img_file = img_file.resize((width, height), Image.ANTIALIAS)
			try:
				fileName = os.path.splitext(aFile)[0] #without file extension
				img_file.save(subdirectory+"/"+ fileName +"_resize.png",format="png", 
											optimize=True, 
											quality=100, 
											progressive=True)
				for i in os.listdir(img_dir):
					if i.endswith('_resize.png'):
						print i
						src_file = os.path.join(img_dir, i)
						dst_file = os.path.join(subdirectory, i)
						shutil.move(src_file, dst_file)
				#print img_files
			
			except IOError:
				print "exception saving file ", aFile

#img_dir = "C:/Users/Bears/Downloads/Ant_Videos"
root = Tkinter.Tk()
root.withdraw() # remove main app window in background
img_dir = tkFileDialog.askdirectory(parent=root,initialdir="C:/",title='Please select a directory')
print "Selected directory: ", img_dir
image_format = raw_input('Enter a file format: ')
print image_format
scale_img = int(input('Enter a scale percent (0-100): '))

print "resizing %s..." %(image_format)
if scale_img == 100:
	print "scale of 100 has no effect, exiting program"
else:
	convert_jpg(img_dir, image_format, scale_img);
print "...done"

