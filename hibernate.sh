"""
Hibernate

This Bash Script will hibernate your PC after specified time in minutes. 
Okay, you're must be wondering what for? When I go to bed, I like to leave my laptop playing my favorite music as I sleep off. 
So, I need it to hibernate after say 1 hour, so that the battery is not drained or doesn't suddenly shutdown. Yeah, certainly not for everyone! 

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
@Usage: hibernate mins
"""

#! /bin/sh

#! /bin/sh
#sleep the pc after these mins

#mins=30
if [ $# -eq 0 ]; then
echo "Usage: $0 -[mins]"
else
	if [ "$UID" -ne 0 ]; then
		echo "you must be root to execute this cmd"
		exit 0
	else
		mins="$1"
		echo "pm-suspend" | at now +"$mins" min
	fi
fi

exit 0












