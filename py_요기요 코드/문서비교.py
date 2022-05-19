from re import I


Old_file = open("dev_CheckDong_json_2.txt", 'r',encoding="UTF-8")
New_file = open("New.txt", 'r',encoding="UTF-8")

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

# 한바퀴 돌리고 싶다.
#
 #if (i == )
# 이게 하나다 
def Old_list_def(Old_lines, Old_list, Old_list_dong): 
 while True:
  for line in Old_lines: 
    split_line=line.split()
    if (len(split_line) >= 1):   
        a = split_line[0]
        if (a== '"city":'): 
            Old_list
            continue
        if (a== '"gu":'):   
            Old_list
            continue
        if (a== "dong"):   
            continue
        Old_list.append(a) 
        if (a== "]"):
           print( Old_list +  [Old_list_dong] )
           #print(Old_list)  
        if (a== "done"):
            break
        #열개씩 돌려야지 
        #재귀함수 

           #print(Old_list) #dong을 리스트로 출력 확인
    #return Old_list_dong
        
for line in Old_lines:
#for문으로 조건식을 주어서 또다시 돌림

    Old_list_def(Old_lines, Old_list, Old_list_dong)
#print(Old_list+ [Old_list_dong])

        #Old_list_dong.append(a)
         #Old_list_gu = Old_list + [Old_list_dong] 
#Old_list.append(Old_list_dong)
#print(Old_list)        
#리스트를 분리
#리스트를 [], [], [] 
#리스트를 리스트로 또다시 묶기 
        
