from lib2to3.pgen2.pgen import DFAState
from re import I


Old_file = open("dev_CheckDong_json.txt", 'r',encoding="UTF-8")
New_file = open("20220401_법정동행정동모두(정규식표현 추가).json", 'r',encoding="UTF-8")

Old_lines = Old_file.readlines()
New_lines = New_file.readlines()

city_list = []
gu_list = []
city2_list = []
gu2_list = []
Old_list = []
Old_list_dong = []
Old_list_line = []
# 파일1 동의 값을 추출
# Old[i] = Old_list 담기
Old_list_gu = []
New_list = []
# 한바퀴 돌리고 싶다.
#
 #if (i == )
# 이게 하나다 
#def Old_list_def(Old_lines, Old_list, Old_list_dong): 
# while True:
num = 0
for i,line in enumerate(Old_lines):
    split_line=line.split()
    #print(split_line)
    if (len(split_line) >= 1):   
        B = split_line[0]
    if (B == '},'):
         # continue
        num= num+ 1  
        #print(num)    
        # 
num2 = 0
for i,line in enumerate(New_lines):
    split_line=line.split()
    #print(split_line)
    if (len(split_line) >= 1):   
        C = split_line[0]
    if (C == '},'):
         # continue
        num2= num2+ 1  
        #print(num)     
#print(num)
# json 파일 안에 있는 객체의 숫자 num
i = 0 
#Old_list_dong = list(range(0,int(num)))
Old_list_dong = []
#for i in range(3):
 #for j in range(2):
  #  Old_list[i][j] = 0
for i in range(num):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(3):
        line.append(0)     # 안쪽 리스트에 0 추가
    Old_list.append(line)         # 전체 리스트에 안쪽 리스트를 추가
    
i = 0 
#New_list_dong = list(range(0,int(num2)))
New_list_dong = []
#for i in range(3):
 #for j in range(2):
  #  Old_list[i][j] = 0
for i in range(num2):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(3):
        line.append(0)     # 안쪽 리스트에 0 추가
    New_list.append(line)         # 전체 리스트에 안쪽 리스트를 추가

#print(Old_list)


# old 파일 리스트로 변환
i = 0
for line in Old_lines: 
  if (num != i): 
    Old_split_line=line.split()
    #print(split_line)
    if (len(Old_split_line) >= 1):   
        a = Old_split_line[0]
        if (a== '"city":'): 
            #print(split_line[1])
            #print(i)
            Old_list[i][0] = Old_split_line[1]
            #Old_list[0].append(split_line[1])
            continue
        elif (a== '"gu":'): 
            Old_list[i][1] = Old_split_line[1]
            #Old_list[0].append(split_line[1])
            continue
        #elif(len(a) >= 2):
        else:
            Old_list_dong.append(a)
            if (a== '},'):
                Old_list[i][2] = Old_list_dong
                Old_list_dong = []
                i = i + 1
                #break # 여기서 멈추고 다시 두번째 루프를 돌아라
                
# New 파일 리스트로 변환
i = 0
for line in New_lines: 
  if (num2 != i): 
    New_split_line=line.split()
    #print(split_line)
    if (len(New_split_line) >= 1):   
        a = New_split_line[0]
        if (a== '"city":'): 
            #print(split_line[1])
            #print(i)
            New_list[i][0] = New_split_line[1]
            #Old_list[0].append(split_line[1])
            continue
        elif (a== '"gu":'): 
            New_list[i][1] = New_split_line[1]
            #Old_list[0].append(split_line[1])
            #print(New_list[i][1])
            continue
        #elif(len(a) >= 2):
        else:
            New_list_dong.append(a)
            if (a== '},'):
                New_list[i][2] = New_list_dong
                New_list_dong = []
                i = i + 1
                #break # 여기서 멈추고 다시 두번째 루프를 돌아라


            #Old_list[i][2] = (Old_list_dong)
        
            #break
#print(Old_list[1][2])
        #if (a == '"dong":'):
         # continue
           
          #old_list.appen(a)
          #break
           #print( Old_list +  [Old_list_dong] )
           #print(Old_list)  
        #if (a== "done"):
         #   break
        #열개씩 돌려야지 
        #재귀함수 

           #print(Old_list) #dong을 리스트로 출력 확인
    #return Old_list_dong

## 전체 주석 처리 ctrl+ K+ C


f1 = open("기존과 동일한 행정동법정동.txt", 'w',encoding = 'utf-8')

#시와 구, 동 모두 동일한 중복값을 추출
#변경되지 않은 사항 텍스트 파일
#city: 
#gu:
#dong:
new_num = 0
old_num = 0  
si_gu_dong_line = []
si_gu_dong_list = [] 
set_list_dong = []
si_gu_dong = []
i = 0
j = 0 
for j in range(num2):
 if (num2 != new_num):   
    for i in range(num):
        if (num != old_num):   
            if New_list[j][0] == Old_list[i][0]: 
                if New_list[j][1] == Old_list[i][1]:
                   #print (Old_list[i][1])
                   city = "city: " + New_list[j][0] +"\n"
                   f1.write(city)
                   gu = "gu: " + New_list[j][1] +"\n"
                   f1.write(gu)
                   #print(gu)
                   #f1.write(gu)
                   #print(gu)
                   O = Old_list[i][2]
                   N = New_list[j][2]
                   dong_name = "dong: \n"
                   f1.write(dong_name)
                   si_gu_dong_line = list(set(O) & set(N))
                   #si_gu_dong = si_gu_dong_line[0]
                   for dong in si_gu_dong_line:
                       if dong == "},":
                          continue
                       elif dong == "{":
                          continue  
                       elif dong == '"dong":':
                          continue      
                       elif dong == "]":
                          continue
                       elif dong == "[":
                          continue  
                       si_gu_dong= "  " + dong + "\n"
                       f1.write(si_gu_dong)  
                   f1.write("\n") 
        old_num = old_num + 1
 new_num = new_num + 1

#print(si_gu_dong)                        
#시는 같으나, 구가 다를 경우의 NEW의 값을 추출
# 변경사항 텍스트 파일

f2 = open("동 업데이트 행정동법정동.txt", 'w',encoding = 'utf-8')

new_num = 0
old_num = 0  
si_gu_dong_line = []
si_gu_dong_list = [] 
set_list_dong = []
si_gu_dong = []
i = 0
j = 0 
for j in range(num2):
 if (num2 != new_num):   
    for i in range(num):
        if (num != old_num):   
            if New_list[j][0] == Old_list[i][0]: 
                if New_list[j][1] == Old_list[i][1]:
                   city = "city: " + New_list[j][0] +"\n"
                   f2.write(city)
                   gu = "gu: " + New_list[j][1] +"\n"
                   f2.write(gu)
                   O = Old_list[i][2]
                   N = New_list[j][2]
                   dong_name = "dong: \n"
                   f2.write(dong_name)
                   si_gu_dong_line = list(set(N)-set(O))
                   #si_gu_dong = si_gu_dong_line[0]
                   for dong in si_gu_dong_line:
                       if dong == "},":
                          continue
                       elif dong == "{":
                          continue  
                       elif dong == '"dong":':
                          continue      
                       elif dong == "]":
                          continue
                       elif dong == "[":
                          continue  
                       si_gu_dong= "  " + dong + "\n"
                       f2.write(si_gu_dong)  
                   f2.write("\n") 
        old_num = old_num + 1
 new_num = new_num + 1

#시는 같으나, 구가 다를 경우의 NEW의 값을 추출
# 변경사항 텍스트 파일

f3 = open("구 업데이트 행정동법정동.txt", 'w',encoding = 'utf-8')

new_num = 0
old_num = 0  
si_gu_dong_line = []
si_gu_dong_list = [] 
set_list_dong = []
si_gu_dong = []
i = 0
j = 0 
Olds = []
News = []
for i in range(num):
    Old = Old_list[i][1]
    Olds.append(Old)
for j in range(num2):
    New = New_list[j][1]
    News.append(New)
#gu_sum = []
gu_sum = list(set(News) - set(Olds))

#print (gu_sum)
num3 = 0
for k,line in enumerate(gu_sum):
    num3 = num3+1
gu_num = 0

         
for j in range(num2):
        if (num2 != new_num):   
            for k in range(num3):
               if (num3 != gu_num):   
                 if New_list[j][1] == gu_sum[k] :
                   city = "city: " + New_list[j][0] +"\n"
                   f3.write(city)
                   gu = "gu: " + New_list[j][1] +"\n"
                   f3.write(gu)
                   O = Old_list[i][2]
                   N = New_list[j][2]
                   dong_name = "dong: \n"
                   f3.write(dong_name)
                   si_gu_dong_line = list(New_list[j][2])
                   #si_gu_dong = si_gu_dong_line[0]
                   for dong in si_gu_dong_line:
                       if dong == "},":
                          continue
                       elif dong == "{":
                          continue  
                       elif dong == '"dong":':
                          continue      
                       elif dong == "]":
                          continue
                       elif dong == "[":
                          continue  
                       si_gu_dong= "  " + dong + "\n"
                       f3.write(si_gu_dong)  
                   f3.write("\n")  
               gu_num = gu_num +1  
        new_num = new_num + 1
   #old_num = old_num + 1 

#시와 구, 동은 모두 동일하나 새로 추가된 값을 추출
#기존 추가사항 텍스트 파일
Newsi = []
Oldsi = []

for i in range(num):
    Old = Old_list[i][0]
    Oldsi.append(Old)

for j in range(num2):
    New = New_list[j][0]
    Newsi.append(New)
si_sum = list(set(Newsi) - set(Oldsi))

#print (gu_sum)
num3 = 0
for k,line in enumerate(si_sum):
     num3 = num3+1
     print(line)
#si_num = 0


f4 = open("시 업데이트 행정동법정동.txt", 'w',encoding = 'utf-8')
       
for j in range(num2):
        if (num2 != new_num):   
            for k in range(num3):
               if (num3 != gu_num):   
                 if New_list[j][0] == si_sum[k] :
                   city = "city: " + New_list[j][0] +"\n"
                   f4.write(city)
                   gu = "gu: " + New_list[j][1] +"\n"
                   f4.write(gu)
                   O = Old_list[i][2]
                   N = New_list[j][2]
                   dong_name = "dong: \n"
                   f4.write(dong_name)
                   si_gu_dong_line = list(New_list[j][2])
                   #si_gu_dong = si_gu_dong_line[0]
                   for dong in si_gu_dong_line:
                       if dong == "},":
                          continue
                       if dong == "{":
                          continue  
                       if dong == '"dong":':
                          continue      
                       if dong == "]":
                          continue
                       if dong == "[":
                          continue  
                       si_gu_dong= "  " + dong + "\n"
                       f4.write(si_gu_dong)  
                   f4.write("\n")  
               gu_num = gu_num +1  
        new_num = new_num + 1
   #old_num = old_num + 1 