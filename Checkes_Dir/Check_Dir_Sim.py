"""Check if the director and the source are similar files."""

# Built-in imports
import filecmp
from filecmp import dircmp
import os
import sys


dir1 = " "
dir2 = " "

dcmp = dircmp(dir1, dir2)

for name in dcmp.left_only:
    #print "diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right)
    print "Left: ", name
for name in dcmp.right_only:
    print "Right: ", name
