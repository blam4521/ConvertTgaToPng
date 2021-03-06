import os, sys
import os.path
import shutil

def change_name(img_dir):

	#renaming textures to textures_small
	src_small = ''.join([img_dir]) + ' '
	dest_small = ''.join([img_dir]) + ' '

	#renamed textures_large to textures
	src_large = ''.join([img_dir]) + ' '
	dest_large = ''.join([img_dir]) + ' '
	
	try:
		if os.path.exists(src_small):
			print 'renaming %s textures to textures small' %src_small
			os.rename(src_small, dest_small)
			print '..renamed textures to textures small successfully'
		if os.path.exists(src_large):
			print 'renaming %s textures_large to textures' %src_large
			os.rename(src_large, dest_large)
			print '...renamed large textures to textures succesfully'
	except:
		print 'ERROR, file path has already been renamed'

if __name__ == "__main__":
	f = open('test.txt','r')
	for line in f:
		img_dir = line.rstrip('\n')
		print 'dealing with this directory: ', img_dir
		change_name(img_dir)
