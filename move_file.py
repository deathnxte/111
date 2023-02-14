import os
import shutil
from_dir='C:/Users/mitta_ck4oqhq/OneDrive/Desktop/images/folder'
to_dir='C:/Users/mitta_ck4oqhq/OneDrive/Desktop'
list_of_files= os.listdir(from_dir)
#print(list_of_files)
for i in list_of_files:
    name,ext=os.path.splitext(i)
    print(name,ext)
