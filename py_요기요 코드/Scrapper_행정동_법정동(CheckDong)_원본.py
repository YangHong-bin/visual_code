# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:16:02 2021

@author: Park Ihn
"""
import json
from collections import OrderedDict
import csv
from datetime import datetime

#input file open
inputCsv = open("G:\내 드라이브\코드\py_요기요 코드\국토교통부_전국 법정동_20211217.csv","r",encoding="cp949")
rd = csv.reader(inputCsv)
lines = list(rd) #list from csv file lines


city=''
gu=''

del lines[0]

bIsSiUpdate = False
bIsGuUpdate = False

fileList = []
tempDong = []
# 구 동 값 모두 없고 시 값만 있을 

for l in lines: 
    if(l[5]==l[1]):
        bIsSiUpdate = True
    elif(l[5]==l[2]):
        bIsGuUpdate = True
    if(bIsSiUpdate):
        bIsSiUpdate= False
        city = l[5] #시 값 update
        continue
    else:
        if(bIsGuUpdate):
            if(len(tempDong) != 0):
                MeetingRecord = OrderedDict()
                MeetingRecord["city"] = city
                MeetingRecord["gu"] = gu
                MeetingRecord["dong"] = tempDong
                fileList.append(MeetingRecord)
                tempDong=[]     
            bIsGuUpdate=False
            gu = l[5]
        else:
            if((l[3]!='') and (l[3] not in tempDong) ):
                tempDong.append(l[3])
            if(l[5] not in tempDong):
                tempDong.append(l[5])
    
        
MeetingRecord = OrderedDict()
MeetingRecord["city"] = city
MeetingRecord["gu"] = gu
MeetingRecord["dong"] = tempDong
fileList.append(MeetingRecord)
tempDong=[]        

now = datetime.now()
with open("output"+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+"_법정동행정동모두.json",'w',encoding = 'utf-8') as f:
    json.dump(fileList, f, ensure_ascii=False, indent="\t")

        
    
print("Complete\n");
inputCsv.close()

