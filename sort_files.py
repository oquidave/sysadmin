"""


"""


import os
from fnmatch import fnmatch
from shutil import move
from time import sleep

dir_path="/source/directory"
dest_path="/destination/directory"
for dirpath, dirs, files in os.walk(dir_path):
  for file in files:
    print file
    if fnmatch(file, "*.your_file_extension"):
      file_fullpath = os.path.join(dirpath, file)
      move(file_fullpath, dest_path)
      print "Moved movie file: : %s " % file_fullpath
      sleep(2)
      
