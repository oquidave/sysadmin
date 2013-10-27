"""    BigDogs
    THis script scans for the largest files in in any directory
    Copyright (C) 2013  <David Okwii>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""



import os

#get the size of this file
def get_size(start_path = '.'):
    total_size = 0
    files = {}
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
	    if os.path.exists(fp):
            	file_size = os.path.getsize(fp)
		files[file_size] = fp
		print fp 
		total_size += file_size
    return total_size, files

#format file size into human readable format
def format_size(size):
	if size < 1024:
		#format to bytes
		size = "%dB" %(size)
		return size
	if size >=1024  and size <= 1024*1024:
		#format size to KB
		size = size / 1024
		return "%dKB"% size
	elif size >= 1024*1024 and size <= 1024*1024*1024:
		#format size to MB
		size = size / (1024*1024)
		return "%dMB" % size
	#and size <= 1024*1024*1024*1024
	elif size >= 1024*1024*1024:
		#format size to GB
		size = size / (1024*1024*1024)
		return "%dGB" % size

print "pliz type exit to exit prog at any time"
while(True):
	start_path = raw_input("pliz enter your path >>> ")
	n = input("pliz enter no of files for the biggest files you want to see >>>")
	if start_path != "exit":
		total_size, files = get_size(start_path)
		#sort the file sizes from biggest to smallest
		file_sizes = sorted(files, reverse=True)
		print "\n\n ###THESE ARE THE BIGGEST %d FILES ### \n" % n
		for file_size in file_sizes[:n]:
			file_path = files[file_size]	
			file_size = format_size(file_size)
			print "%s: %s" %(file_size, file_path)
		print "\n###################################"
	else:
		selection = raw_input("do you really want to quit?(yes/no)")
		if selection == "no":
			continue
		else:
			break
		
