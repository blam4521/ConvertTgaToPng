"""Move Files from one area to another."""

# Built-in imports
import logging
import os
import shutil
import sys

# Third-party imports
from PIL import Image, ImageFile
import Tkinter
import tkFileDialog


def move_tga(img_dir):
    """Move targa image files around.

    Args:
        img_dir(str): Path to images being moved.

    """

    large_subdir = img_dir + "/texture_large"
    parent_dir = img_dir

    if os.path.exists(large_subdir):
        logging.info('there is already a folder named %s' % (large_subdir))
        for aFile in os.listdir(large_subdir):
            if aFile.endswith('tga'):
                logging.info('Found tga: %s', aFile)
                src_file = os.path.join(large_subdir, aFile)
                dst_file = os.path.join(parent_dir, aFile)
                logging.info("copying file: " + aFile)
                shutil.copy(src_file, dst_file)

                # Building file name to remove which is a string.
                fileName = os.path.splitext(aFile)[0]  # without file extension
                # Concatanating string.
                pngToRemove = img_dir + "/" + fileName + ".png"

                # Removes png.
                if os.path.lexists(pngToRemove):
                    print "removing file: "+pngToRemove
                    os.remove(pngToRemove)


f = open('a_list.txt', 'r')
for line in f:
    img_dir = line.rstrip('\n')
    print "dealing with this directory:", img_dir
    move_tga(img_dir)
    print "...moving done"
