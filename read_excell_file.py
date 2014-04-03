"""
Example python to read from a 3 column excel file

We use the xlrd module here to read from excel 97/2000/2003
 Download from the python website

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

#!/usr/bin/env python
import xlrd

#create the book object
book = xlrd.open_workbook(source_file)
for sheet_name in book.sheet_names():
  #walk through each sheet
   sheet = book.sheet_by_name(sheet_name)
   max_rows = sheet.nrows
   max_cols =  sheet.ncols
   for rownum in range(max_rows):
     this_row = sheet.row_values(rownum)
     first_col = str(this_row[0])
     second_col = str(this_row[1])
     third_col = str(this_row[2])
     
