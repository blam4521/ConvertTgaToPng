import os, sys
import os.path
import shutil

def move_large_texture(img_dir):


	dest = ''.join([img_dir]) + '/textures_large/'
	src = ''.join([img_dir]) +  '/textures/texture_large'
	
	print 'destination where you want it to be: ', dest
	print 'source of where the folder is: ', src

	
	if not os.path.exists(dest):
		print 'moving texture_large subdirectory...'
		#os.makedirs(dest)
	
	#for item in os.listdir(src):
	#	print 'dealing with this file..',item
	#	src_file = src + '/' + item
	#	print src_file
	    
	
		try:
			shutil.move(src, dest)
			#print '...copy done'
		except:
			print 'error'
    
	#try:
	#    print 'removing old dir'
	#    shutil.rmtree(src)
	#except:
	#	print 'Could not delete Dir'
    
		

if __name__ == "__main__":
    f = open('a_list.txt', 'r')
    for line in f:
    	img_dir = line.rstrip('\n')
    	print 'dealing with this directory: ', img_dir
    	move_large_texture(img_dir)
    	print '....moving done'

