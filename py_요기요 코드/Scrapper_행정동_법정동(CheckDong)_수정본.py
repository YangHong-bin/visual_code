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
inputCsv = open("국토교통부_전국 법정동_20211217.csv","r",encoding="cp949")
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
for num,l in enumerate(lines) : 
    if(num == 0):
        city = l[1]
        gu = l[2]
        if((l[3]!='') and (l[3] not in tempDong) ):
                    tempDong.append(l[3])
        if(l[4] not in tempDong):
                    tempDong.append(l[4])
        n = l   
        print(n)                 
    elif(num > 1):
        if(l[1]!=n[1]): #시의 값 갱신
            city = l[1]
            print(city)
            n = l
        else: #시의 값이 갱신이 안될 때
            if( (l[2]!=n[2]) and (l[2] != '') ):  #구의 값 갱신    
                gu = l[2]                 
                if(len(tempDong) != 0):
                    MeetingRecord = OrderedDict()
                    MeetingRecord["city"] = city
                    MeetingRecord["gu"] = gu
                    MeetingRecord["dong"] = tempDong
                    fileList.append(MeetingRecord)
                    tempDong=[]  
            else: #구의 값이 갱신이 안 될때
                if((l[3]!='') and (l[3] not in tempDong) ):
                    tempDong.append(l[3])
                if((l[4]!='') and(l[4] not in tempDong) ):
                    tempDong.append(l[4])
            n = l  
          
        
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

