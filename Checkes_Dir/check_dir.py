import os, sys
import os.path
import shutil

def check_name(img_dir):

	

	src_small = img_dir + '/textures_small/'
	#src_large = img_dir + '/textures_large'

	try:
		if not os.path.exists(src_small):
		#if os.path.exists(src_small):
			print img_dir

			

	except:
		print 'There folders named textures_small'



if __name__ == '__main__':
	f = open('a_list.txt', 'r')
	for line in f:
		img_dir = line.rstrip('\n')
		#print 'dealing with this director ', img_dir
		check_name(img_dir)
	print "...done"