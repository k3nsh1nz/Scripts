#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
import json
import gspread
import smtplib
from datetime import datetime
from time import time
from oauth2client.client import SignedJwtAssertionCredentials
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# authorize google
json_key = json.load(open('/home/path/k/token.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
# access google sheets
worksheet = gc.open("Tien An Nhom").sheet1
# tinh tong tien 
s1 = 0
s2 = 0
s3 = 0
s4 = 0
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
# tinh toan tien 
# a Manh, a Quy, a Duc Anh, a Thang, a Toan, a Ngan
for j in xrange((row-9),(row+1)):
    s1 += int(worksheet.acell("C"+str(j)).value) * int(worksheet.acell("H"+str(j)).value)
for j in xrange((row-9),(row+1)):
    s2 += int(worksheet.acell("D"+str(j)).value) * int(worksheet.acell("H"+str(j)).value)
for j in xrange((row-9),(row+1)):
    s3 += int(worksheet.acell("E"+str(j)).value) * int(worksheet.acell("H"+str(j)).value)
for j in xrange((row-9),(row+1)):
    s4 += int(worksheet.acell("F"+str(j)).value) * int(worksheet.acell("H"+str(j)).value)

# ngay gui mail
date=worksheet.acell("B"+str(row)).value

##### function send mail ######
def send_mail(toaddr,total,date):
    fromaddr = "xxxxx@gmail.com"
    clgt = "XXXXXX"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Tiền ăn nhóm "+date
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr,clgt)
#    body = "Tiền ăn nhóm:\nFile docs: http://xxxxxxxxxxxxxxxxxxxxxxxxx.com\n"+"Số tiền anh đóng mới là: "+str(total) +"k"
    body = "Tiền ăn nhóm: "+date+"\nFile docs: http://xxxxxxxxxxxxxxxxxxxxxxxxx.com\n"+"Số tiền anh đóng mới là: "+str(total) + "k"+"\n------------------------------------\nXXXXXX\nVXXXXX\nSTK: XXXXXX"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.close()
##### end function ######
# kiem tra ngay tiep theo, neu da cap nhat roi thi thoi k gui mail
if worksheet.acell("H"+str(row+1)).value:
    pass
    #send_mail("xxxx@gmail.com","NO update",date)
else:
    send_mail("xxx@vgmail",s1,date)
