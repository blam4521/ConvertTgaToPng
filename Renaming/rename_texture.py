"""Changes the texture name into something else."""

# Built in imports
import os
import sys
import os.path
import shutil


def change_texture_name(img_dir):
    """Change texture name into some other format.abs

    Args:
            img_dir (str): Path to the image directories.

    """
    for img in os.listdir(img_dir):
        if img.endswith('.tga'):
            fileName = os.path.splitext(img)[0]
            ext = '.tga'
            new_file = '' .join([fileName, '_v001.0000', ext])
            os.rename(os.path.join(img_dir, img),
                      os.path.join(img_dir, new_file))


if __name__ == '__main__':
    f = open('test.txt', 'r')
    for line in f:
        img_dir = line.rstrip('\n')
        print 'dealing with this directory: ', img_dir
        change_texture_name(img_dir)
