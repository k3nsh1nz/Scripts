#!/usr/bin/python
# -*- coding: utf-8 -*-
# set cronjob
# 0 13 */5 * * python notification_tien_an.py
#
import json
import gspread
import smtplib
from datetime import datetime
from time import time
from oauth2client.client import SignedJwtAssertionCredentials
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

time_start = time()
f1 = open("/root/a.txt","a")
# authorize google
json_key = json.load(open('/path/../token.json'))
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
s5 = 0
s6 = 0
# tim cac o co stt la 10
k = worksheet.findall("10")
# kiem tra cac o cuoi cung cua cac dot tien an, luu vao mang
moneys =[]
for i in k:
	money = worksheet.acell("J"+str(i.row)).value
	if money:
		moneys.append(worksheet.acell("J"+str(i.row)))
	
# lay dia chi hang o cuoi cung cua dot tien an
row = moneys[-1].row
# tinh toan tien 
# a Manh, a Quy, a Duc Anh, a Thang, a Toan, a Ngan
for j in xrange((row-9),(row+1)):
	s1 += int(worksheet.acell("C"+str(j)).value) * int(worksheet.acell("J"+str(j)).value)
for j in xrange((row-9),(row+1)):
	s2 += int(worksheet.acell("D"+str(j)).value) * int(worksheet.acell("J"+str(j)).value)
for j in xrange((row-9),(row+1)):
	s3 += int(worksheet.acell("E"+str(j)).value) * int(worksheet.acell("J"+str(j)).value)
for j in xrange((row-9),(row+1)):
	s4 += int(worksheet.acell("F"+str(j)).value) * int(worksheet.acell("J"+str(j)).value)
for j in xrange((row-9),(row+1)):
	s5 += int(worksheet.acell("G"+str(j)).value) * int(worksheet.acell("J"+str(j)).value)
for j in xrange((row-9),(row+1)):
	s6 += int(worksheet.acell("H"+str(j)).value) * int(worksheet.acell("J"+str(j)).value)

##### function send mail ######
def send_mail(toaddr,total):
	fromaddr = "xx@gmail.com"
	clgt = "xxx"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Tiền ăn nhóm"
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(fromaddr,clgt)
	body = "Tiền ăn nhóm:\nFile docs: xxxx\n"+"Số tiền: "+str(total) +"k"
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.close()
##### end function ######
# kiem tra ngay tiep theo, neu da cap nhat roi thi thoi k gui mail
if worksheet.acell("J"+str(row+1)).value:
	pass
else:
	send_mail("yyyy@gmail.com",s2)
	now = time()
	msg = "Done at "+str(datetime.now())+"\nTime process:"+str(now-time_start)+"\n"
	f1.write("-------------------------------------\n")
	f1.write(msg)

f1.close()
