"""
Remote SSH command

This script lets your execute a command on a remote box from a local machine via SSH

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
@dependencies: Python 2.7 or higher, Paramiko module

"""


#!/usr/bin/env python

import paramiko #ssh module
import subprocess #module to execute commands 

 
hostname = 'hostname'
username = 'username'
password = 'secret'

cmd = 'some bash command'

#create ssh object
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#connect
try:
    ssh.connect(hostname,username=username, password=password)
except:
    print 'failed to connect to remote host'
#now go ahead and excute your command
try:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    cmd_output = stdout.read()
    print cmd_output
except:
    print 'failed to execute the command'
