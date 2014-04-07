#!/usr/bin/env python
"""
Copy files to a remote box using ssh or secure ftp

Copyright (C) 2011 <David Okwii>

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
@Date: 2011
@Email: oquidave@gmail.com
"""

import paramiko
import os

"""file details"""
src_file = "/path/to/src/file"
dest_dir = "/path/to/dest/dir/on/remote/server"

"""remote server details"""
hostname, username, password = "server_hostname", "username", "secret"

"""connect to remote box using ssh"""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
#using put, copy file to remote server
ftp = ssh.open_sftp()
try:
	ftp.put(src_file, dest_dir)
	print "successfully copied file to remote server"
except:
        print "failed to copy file to remote server"
    ftp.close()