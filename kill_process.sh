#! /bin/sh
<<'COMMENT'
Kill Process

Bash Script to kill a process running on specific port. Yes, you'll need it to stop non-standard servers for instance django server, app engine server etc 
where you can't use something like "sudo service apache stop".
Usually, you would first get the pid of the process/server running on a specific port using maybe "netstat", then you use the "kill" cmd to stop the process
running that pid. That's long stuff. 

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
@Usage: kill_process port 
@comments: you should make this script executable with `chmod +x script.sh` and run it with `./script.sh` or use bash script.sh 


COMMENT

#! /bin/sh


if [ $# -eq 0 ]; then
	echo “Usage: $0 [port number]
	exit
else
if [ $EUID -ne 0 ]; then 
	echo "please run this script as root"
	exit
fi
	port="$1"
	#process_pid=`netstat -pant | grep "0 0.0.0.0:$port" | awk '{print $7}' | grep -o -P "\d+"`
	process_pid=`lsof -i :$port | sed -n 2p | awk '{print $2}'`
	echo "process id for process on port $port is: $process_pid" 
	if [ $process_pid ]; then
		kill -9 $process_pid >&2 /dev/null
			if [ $? -eq 0 ]; then
				kill -9 $process_pid
				echo "process running port $port has been stoped"
				exit 0
			fi
	else
		echo "no such process running port $port"
	fi
fi



