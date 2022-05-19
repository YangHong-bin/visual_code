from re import I


Old_file = open("dev_CheckDong_json_2.txt", 'r',encoding="UTF-8")
New_file = open("New.txt", 'r',encoding="UTF-8")

Old_lines = Old_file.readlines()
New_lines = New_file.readlines()

city_list = []
gu_list = []
city2_list = []
gu2_list = []

# 파일1 city,gu 추출
for line in Old_lines:
    split_line=line.split()
        #리스트가 2개 이상인 조건문
        #print(split_line) 
    if (len(split_line) >= 2):            
        if (split_line[0] == '"city":'):
            ci = split_line[1].strip(",") #쉼표제거
            city = ci.strip('"') #쉼표제거
            city_list.append(city)
    if (len(split_line) >= 2):
        if (split_line[0] == '"gu":'):
            gu = split_line[1].strip(",") #쉼표제거
            guname = gu.strip('"') #쉼표제거
            gu_list.append(guname)

# 파일2를 파일1과 비교하여 dong을 list로 저장
for line in New_lines:
    split_line=line.split()
    if (len(split_line) >= 2):            
        if (split_line[0] == '"city":'):
            ci = split_line[1].strip(",") #쉼표제거
            city = ci.strip('"') #쉼표제거    
    for i in city_list:
        if (city == i):
            city_check = "True"
            continue
        else:
            city_check = "False"
    if (len(split_line) >= 2):
        if (split_line[0] == '"gu":'):
            gu = split_line[1].strip(",") #쉼표제거
            guname = gu.strip('"') #쉼표제거
            gu_list.append(guname)
    for i in gu_list:
        if (guname == i):
            gu_check = "True"
        else:
            gu_check = "False"
    #파일1과 파일2가 공통된 city와 gu를 가진 경우 파일2의 Dong을 리스트로 저장
    if (city_check == "True" and gu_check == "True"):
    
#for

#for i in city_list:
        # 시 중복 체크
#        if (city != i):
#            city_list.append(city)
#            print(city)
            
        
                
             