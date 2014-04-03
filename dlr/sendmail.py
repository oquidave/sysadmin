"""
Send email using the smtplib module. Dead simple!!

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
@Usage: python sendmail.py email_server, to, subject, message
"""

#!/usr/bin/env python
import smtplib
import sys

#get values from the cli or you can just add your own
SERVER = sys.argv[1]
FROM = "noreply@%s" % (SERVER)
TO  = sys.argv[2]
SUBJECT = sys.argv[3]
BODY = sys.argv[4]

# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, TO, SUBJECT, BODY)

# Send the mail
try:
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()
    print 'successfully sent the mail'
except:
    print "failed to send mail" 