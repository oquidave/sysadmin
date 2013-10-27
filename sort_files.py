"""
Sort files by file extention 

This script enables you to look for files of a certain extension and moves in to a specified 
destination directory. 
 Copyright (C) 2013 <David Okwii>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA


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
      
