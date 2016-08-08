#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
import json
import gspread
import smtplib
import datetime
from oauth2client.client import SignedJwtAssertionCredentials
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
now = datetime.datetime.now()
today = now.strftime('%m/%d/%Y')


# authorize google
json_key = json.load(open('/home/path/k/token.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
# access google sheets
worksheet = gc.open("Tien An Nhom").sheet1
# tim cac o co stt la 10
k = worksheet.findall("10")
# kiem tra cac o cuoi cung cua cac dot tien an, luu vao mang
moneys =[]
for i in k:
    money = worksheet.acell("H"+str(i.row)).value
    if money:
        moneys.append(worksheet.acell("H"+str(i.row)))
    
# lay dia chi hang o cuoi cung cua dot tien an
row = moneys[-1].row
count = row+1
for i in xrange(row,row+10):
    if (worksheet.acell("B"+str(count)).value):
            count +=1
    else:
        if (now.weekday() < 5):
            worksheet.update_acell(("B"+str(count)), str(today))
            worksheet.update_acell(("C"+str(count)), '1')
            worksheet.update_acell(("D"+str(count)), '1')
            worksheet.update_acell(("E"+str(count)), "1")
            worksheet.update_acell(("F"+str(count)), "1")
            worksheet.update_acell(("G"+str(count)), "4")
            worksheet.update_acell(("H"+str(count)), "40")
            break
print "OK r"
