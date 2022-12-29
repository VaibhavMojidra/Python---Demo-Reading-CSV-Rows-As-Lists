#Reading CSV - Rows As Lists

import csv

f=open('example.csv')

csvData=csv.reader(f)

for row in csvData:
    SID,SNAME,GENDER=row
    print("SID: {}, SNAME: {}, GENDER: {}".format(SID,SNAME,GENDER))
