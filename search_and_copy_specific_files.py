#!/usr/bin/env python
"""
Recursively copy specific files from a specific direcotry to another. 
This interactive script automatically creates destination folders for each file extension in the destination direcotry. 
Haven't done any cross-platform user-validation. Feeling lazy already

Copyright (C) 2014 <David Okwii>

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
@Date: 2014
@Email: oquidave@gmail.com
@Usage: python {this_script_name} 
"""
import os
from fnmatch import fnmatch
from shutil import copy

"""search for files that match certain criteria. 
Meanwhile I failed to optimize this function to work alittle faster!"""
def search(src, extens):
	matched_files = {}
	for exten in extens:
		matched_exten_files = []
		for dir_path, dir, files in os.walk(src):
			for file in files:
				if fnmatch(file, "*."+exten.strip()):
					file_fullpath = os.path.join(dir_path, file)
					matched_exten_files.append(file_fullpath)
		matched_files[exten] = matched_exten_files
	return matched_files

"""copy the file to provided destination folder"""
def cp(src, dest):
	copy(src, dest)
	print "Copied %s --> %s " % (src, dest)

#get user data from interactive shell
src = raw_input("enter yoour source directory. >> ")
dest = raw_input("enter yoour destination directory. >> ")
extens_str = raw_input("Enter file extensions to search separated by commas >> ")
extens = extens_str.split(",")

#get the matched files
matched_files = search(src, extens)
#move each file type to its own directory
for exten, exten_files in matched_files.iteritems():
	#create dest folder for this extension based on the file extension
	dest_exten = dest + "/" + exten.strip()
	os.mkdir(dest_exten)
	for src in exten_files:
		cp(src, dest_exten)

