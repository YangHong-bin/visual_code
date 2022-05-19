from re import I
import json


New_file = open("New.txt", 'r',encoding="UTF-8")

# json 파일 불러와서 딕셔너리로 변환시킨다.
# json.loads는 여러 json 객체를 디코딩 하지 않는다. 주의해야 함!
# loads는 문자열을 읽을 때 쓴다.
# load는 파일을 읽을 때 쓴다.

list= []

#Old_file = open("dev_CheckDong_json_2.json", "r", encoding="UTF-8") 
with open("dev_CheckDong_json_2.json", "r", encoding="UTF-8") as Old_file:
    data = Old_file.read()
    #data = json.load(Old_file)
#szprint(da)
#for line in f.readlines():
 #   print(line)
  #  data = json.loads(line)
   # list.append(data)

#print(list)



#dic_old = Old_file.read()
#data= json.load(dic_old)
#for line in Old_file:
#    list.append(json.loads(line))
  #
  #print(dic_old)
#  Old_json = json.load(Old_file,strict=False)
 
print(data)
#dict_Old_file =json.loads(dic_old)

#for line in Old_file:
  #dict_Old_file =json.loads(line)
  #print(line)

#

#print(dict_Old_file)