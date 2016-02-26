import os, sys
import os.path
import shutil
import filecmp
from filecmp import dircmp
import filecmp

dir1 = "X:/little_charmers2/maya/season1_proj/environments/textures"
dir2 = "X:/little_charmers2/maya/season1_proj/environments/textures_small"

dcmp = dircmp(dir1, dir2) 


for name in dcmp.left_only:
    #print "diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right)
    print "Left: ", name
for name in dcmp.right_only:
    print "Right: ", name