import os
from fnmatch import fnmatch
from shutil import move
from time import sleep

dir_path="/home/oquidave/hdrecovers"
dest_path="/home/oquidave/images"
for dirpath, dirs, files in os.walk(dir_path):
  for file in files:
    print file
    if fnmatch(file, "*.iso"):
      file_fullpath = os.path.join(dirpath, file)
      move(file_fullpath, dest_path)
      print "Moved movie file: : %s " % file_fullpath
      sleep(2)
      
