"""
Seach and Move specific files

This script lets you move specific files from one folder to another. For only lazy guys!! 

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

@Author: David Okwii
@Date: 2013
@Email: oquidave@gmail.com

"""


#!/usr/bin/env python

import os
from fnmatch import fnmatch
from shutil import move

src_dir="/path/to/source/dir"
dest_dir="/path/to/dest/dir/"

#recursively walk through the source directory
for dirpath, dir, files in os.walk(src_dir):
  for file in files:
    #say we want to move movie files only
    if fnmatch(file, "*.mov") or fnmatch(file, "*.mp4") or fnmatch(file, "*.avi") or fnmatch(file, "*.mkv"):
      file_fullpath = os.path.join(dirpath, file)
      move(file_fullpath, dest_dir)
      print "Moved Movie file: : %s " % file_fullpath
      