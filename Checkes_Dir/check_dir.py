"Check the directory if it exists."

# Built-in imports
import os
import sys
import os.path
import shutil


def check_name(img_dir):
    """Check if the directory exists.

    Args:
            img_dir (str): name of the file directory.

    """

    src_small = img_dir + ' '
    #src_large = img_dir + ' '

    try:
        if not os.path.exists(src_small):
            # if os.path.exists(src_small):
            print(img_dir)

    except:
        print 'There folders named textures_small'


if __name__ == '__main__':
    f = open(' ', 'r')
    for line in f:
        img_dir = line.rstrip('\n')
        #print 'dealing with this director ', img_dir
        check_name(img_dir)
    print('...done')
