"""
Example python script to export records from Postgresql table to Excell

Two major modules involved here: psycopg2 which is the python module for interfacing with Postgresql DB and 
xlwt module which is for creating excel  97/2000/2003 files (xlrd reads). Download both of them from the python website

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
@Usage: python postgres_excell_export.py host, database, sql, output_file 

"""

#!/usr/bin/env python

import xlwt #module for writing excel files
import psycopg2 #postgres module
import psycopg2.extras
import sys
import os
#time modules
from datetime import *

#get cli values
host = sys.argv[1]
database = sys.argv[2]
sql = sys.argv[3]
output_file = sys.argv[4]

dbh_stg = "dbname='%s' user='postgres' host='%s'" %(database, host)
dbh = psycopg2.connect(dbh_stg)
# Real Dict Cursor (returns a Dict which can be referenced via named bracket access, or offset)
dict_cursor = dbh.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
dict_cursor.execute(sql)
rownum = dict_cursor.rowcount
if rownum > 0:
    #start the excel write
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Delivery stats')
    #row counter
    i = 0
    #get db results
    rows = dict_cursor.fetchall()
    for row in rows:  
        phonenum = row['phone_number']
        dlrvalue = row['dlrvalue']
        ts_stamp = row['time_stamp']
        
        if dlrvalue == 1 or dlrvalue == 8:
            status = 'Sent'
        else:
            status = 'Not Sent'
        #write these values to the excel colums
        ws.write(i, 0, phonenum)
        ws.write(i, 1, status)
        ws.write(i, 2, ts_stamp)
        #increament the couter
        i = i+1
    #write the excel file
    wb.save(output_file)
    print 'success'