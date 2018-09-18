import os
import sys
import os.path
import shutil


def change_texture_name(img_dir):

    for img in os.listdir(img_dir):
        if img.endswith('.tga'):
            fileName = os.path.splitext(img)[0]
            # building new path
            ext = '.tga'
            new_file = '' .join([fileName, '_v001.0000', ext])
            #print new_file
            print 'renaming %s to %s ' % (img, new_file)
            # try:

            os.rename(os.path.join(img_dir, img),
                      os.path.join(img_dir, new_file))

            # except:
            #	print ("Error, can't rename file")
    print '..renamed textures successfully'


if __name__ == "__main__":
    f = open('test.txt', 'r')
    for line in f:
        img_dir = line.rstrip('\n')
        print 'dealing with this directory: ', img_dir
        change_texture_name(img_dir)
