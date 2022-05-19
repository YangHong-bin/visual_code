# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:16:02 2021

@author: Park Ihn
"""
import json
from collections import OrderedDict
import csv
from datetime import datetime
import re
from turtle import Turtle
#input file open
inputCsv = open("KIKmix.20220401(말소코드포함).csv","r",encoding="cp949")
rd = csv.reader(inputCsv)
lines = list(rd) #list from csv file lines

### GUI 형식으로
### 파일을 선택하면 입력됨
### 

city=''
gu=''

del lines[0]
## 첫행 삭제


bIsSiUpdate = False
bIsGuUpdate = False

fileList = []
tempDong = []
# 구 동 값 모두 없고 시 값만 있을 
# l[0] 법정동코드
# l[1] 시도명
# l[2] 시군구
# l[3] 읍면동
# l[4] 리
# l[5] 순위
# l[6] 생성일자
# 중복시 하나의 시만: 처음에는 기록하나, 그다음부터는 현재의 값과 앞의 값이 같을 때 건너뛰고, 같지 않을 때 기록 
# 중복시 하나의 구만: 시의 값이 같을 때, 처음에는 기록하나, 그다음부터는 현재의 값과 앞의 값이 같을 때 건너뛰고, 같지 않을 때 기록    
# 중복시 하나의 동만: 시의 값과 구의 값이 같을 때, 정규식표현 '제'숫자일 경우 '제'를 삭제한 값을 추가하라

# (서울시 종루고 세종로 )
# L1 시 L2 구 L3 동 L4리명 L5 시 - 구 - 동
si_check = []
MeetingRecord = OrderedDict()
MeetingRecord["city"] = city
MeetingRecord["gu"] = gu
MeetingRecord["dong"] = tempDong

for l in lines:
    
    if(l[5]==l[1]):
        gu_check = [] 
        #print(gu_check)
        bIsSiUpdate= True
       
    if(l[5]==l[2]):  
        gu_check.append(gu)
        check = True
        for gu_list in gu_check:
            if (gu_list == l[5]):        
                    check = False 
                    #print(gu_list)        
        if(check): 
            bIsGuUpdate = True
            gu = l[5] 

    if(bIsSiUpdate):    
        bIsSiUpdate= False
        city = l[5] #시 값 update
        continue 
    else:
        if(bIsGuUpdate): #구의 값이 행정동과 법정동이 같을 때          
            tempDong=[] 
            MeetingRecord = OrderedDict() #순서대로 넣어라
            MeetingRecord["city"] = city #시의 값을 넣고
            MeetingRecord["gu"] = gu #구의 값을 넣고
            MeetingRecord["dong"] = tempDong  
            fileList.append(MeetingRecord)
            #print(fileList)        
            bIsGuUpdate = False        
        else:
            if((l[3]!='') and (l[3] not in tempDong) ): # 정규식 추가하기
                #동의 값이 빈칸이 아니고, 동의 값이 tempdong에 없을 때
                m = re.search('제\d', l[3])
                if m == None:
                # 문자열 '제1'의 값이 매치되는 값이 없다면 동의 값을 그대로 삽입 
                   tempDong.append(l[3])
                elif m != None: 
                   n = m.start()
                   if n >= 1:
                # 문자열 '제1'의 값이 있고, 첫글자가 '제' 아닐 때     
                    mm =     re.search('제제',l[3])
                   if (mm == None):
                       ## '거제제1동'같은 문자열이 없다면,
                      k= re.sub(r'제', "", l[3])
                      tempDong.append(l[3])
                      ## '묵제1동' 삽입
                      tempDong.append(k)
                      ## '묵1동' 삽입
                   else:
                      ## '게제제1동과 같은 문자열이 있다면, 거제1동으로 삽입
                      k= re.sub(r'제제', "제", l[3])
                      tempDong.append(l[3])
                      tempDong.append(k)
                   #  '거제제1동' 삽입
                   #  '거제1동' 삽입
                   #  첫글자가 '제'가 아닌 문자열에서 '제'를 삭제한 '묵동1동'을 삽입              
                   # '묵동제1동'과 '묵동1동'의 값을 동시에 추가
            if(l[5] != ""):
                if(l[5] not in tempDong):   
                    tempDong.append(l[5])
        #if(l[5] not in tempDong):   
         #       tempDong.append(l[5])        
   
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

