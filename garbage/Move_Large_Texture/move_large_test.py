import os
import shutil

for name in os.walk('.').next()[1]:

    dest = os.path.dirname(os.path.join(os.path.abspath(name),name))+' '
    src  = os.path.dirname(os.path.join(os.path.abspath(name),name))+' '
    print(dest)

    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for item in os.listdir(src):
        print(item)
        src_file = src + item
        try:
            shutil.copy2(src_file, dest)
        except:
            print('error')

    try:
        shutil.rmtree(src)
    except:
        print('Could not delete Dir')

