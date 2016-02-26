import os, sys
import os.path
import shutil



def move_tga(img_dir):

	
	large_subdir = img_dir + "/texture_large"
	parent_dir = img_dir


	if os.path.exists(large_subdir):
		print 'there is already a folder named %s'%(large_subdir)
		for aFile in os.listdir(large_subdir):
			if aFile.endswith('tga'):
				print "Found tga:" + aFile
				src_file = os.path.join(large_subdir, aFile)
				dst_file = os.path.join(parent_dir, aFile)
				print "copying file: " + aFile
				shutil.copy(src_file, dst_file)

				#building file name to remove which is a string
				fileName = os.path.splitext(aFile)[0] #without file extension
				#concatanating string
				pngToRemove = img_dir + "/" + fileName + ".png"
				
				#removes png
				if os.path.lexists(pngToRemove):
					print "removing file: "+pngToRemove	
					os.remove(pngToRemove)

f = open('a_list.txt','r')
for line in f:
	img_dir = line.rstrip('\n')
	print "dealing with this directory:", img_dir
	move_tga(img_dir);
	print "...moving done"
		


