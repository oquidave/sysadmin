"""
Phone number formatter 

Formats phone numbers into the standard format. This is strictly for mobile phones mainly in Uganda. 

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
@Usage: python phone_formater.py 
"""

#!/usr/bin/env python
import re

""" 
format phone numbers
phone numbers should take the form of 256{network-prefix}{numeric-numbers} e.g
256754123456
however numbers are uploaded in all sorts of formats by users e.g
the most common are ;
0754123456(common)
754123456 (zero missing)
+256754123456(plus sign added)
+256-754-123-456(dashes are added)
0754-123-456

some numbers are also invalid for example when not all the digits are 12 digits after formatting.
for these, reject them
"""


phone = raw_input('Enter phone no    ')
print phone

formated_phone = ''
digits_only_pattern = '\d+'
re_obj = re.compile(digits_only_pattern)
match = re_obj.search(phone)
if not match: 
  print "This phone number does not contain digits only!"
else:
    for matched in re_obj.findall(phone):
        #print matched
        "piece it all matched digits togather"
        formated_phone += matched
    #print formated_phone
    
    #Now lets count the digits in the formated number
    formated_phone_count = len(formated_phone)
    if formated_phone_count > 12:
        print "phone number is invalid"
    if formated_phone_count == 12:
        "Then phone number is valid and had country code prefix like 256"
        print formated_phone
    if formated_phone_count < 12:
        """this could be something like 07548198, so lets just get number prefix"""
        ntwk_no_prefix = formated_phone[-9:]
        ntwk_no_prefix_count = len(ntwk_no_prefix)
        if ntwk_no_prefix_count == 9:
            no_prefix = formated_phone[-6:]
            ntwk_prefix = formated_phone[-9:-7]
            if not ntwk_prefix.startswith('0'):
                "now append country prefix 256 for ugandan numbers"
                #ntwk_prefix_pattern = '([77] | [78] | [39] | [70] | [71] | [75] | [79])'
                ntwk_prefix_pattern = '7[01589]|39'
                re_obj = re.compile(ntwk_prefix_pattern)
                match = re_obj.search(ntwk_prefix)
                if match:
                    formated_phone = '256'+ntwk_no_prefix
                    print formated_phone
                else:
                    print "perhaps international no"
                    print formated_phone
            else:
                print "your number is invalid"
        else:
            print "your number is invalid"
    
