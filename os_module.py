"""
The Python os module. Provides low-level access to the OS

See how awesome python is when working with the OS

@Author: David Okwii
@Date: 2013
@Email: oquidave@gmail.com

Disclaimer: You screwup your files, am not concerned! 

"""

import os
from fnmatch import fnmatch #file matching module
from shutil import move #file operation module

#get current working dir path
cwd = os.getcwd()

#parent working dir path
os.path.dirname(os.getcwd())

#get name of current working dir
os.path.basename(os.getcwd())

#test if dir
os.path.isdir(os.getcwd())

#change current working directory
os.chdir("/dir/to/change/to/")

#make a directory
os.mkdir("/path/of/new/dir")

#rename 
os.rename("/path/to/old/dir", "/path/to/new/dir")

#remove dir a directory/file
os.rmdir("/path/to/dir/to/remove")
os.remove("/path/to/file/to/remove")

#recursively copy a dir
shutil.copytree("/path/to/src/dir", "/path/to/destination/dir")

#move file
move("/path/to/source/file", "/path/to/destination/file")

#archive folder
shutil.make_archive("/destination/path/to/archive","tar", "/source/dir/to/archive")

#list directories in the current working dir
os.listdir(os.getcwd())

#list the directories in the current working dir as a list
for dir in os.listdir(os.getcwd()):
  print dir 
  
#recursively walk through directories
for dirpath, dir, files in os.walk("/path/to/source/dir"):
  for file in files:
    print file
    #get the fully file path
    file_fullpath = os.path.join(dirpath, file)
    #search for a specific file with a certain extention
     if fnmatch(file, "*.mov"):
       print "yes there are .mov  files"
       #move file from one dir to another
       move(file_fullpath, dest_path)
       #remove the file
       ##os.remove(file_fullpath)
  