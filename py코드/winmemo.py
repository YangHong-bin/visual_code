
import tkinter as tk
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import StringVar, ttk
from tkinter import filedialog
from tkinter.constants import COMMAND, END
from tkinter import scrolledtext
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime
from moviepy.video.VideoClip import ColorClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube 
import os
import shutil
import glob
import moviepy.editor as mp
import time
from cefpython3 import cefpython as cef
import sys
import platform
from tkinter import messagebox
from tkinter import scrolledtext
from datetime import date
from collections import defaultdict
import string
from threading import Thread
from pygame import mixer
###자동설치################################################################################

#1. 꿀뷰 
#2. 반디집
#3. 알pdf
#4. 비주얼 코드
#5. 고클린
#6. 카카오톡
#7. 크롬
#8. 밀러의 서재
#9. shxmvoem3
#10. 파이썬 모듈 자동설치
#11. 구글 드라이버 

###주식################################################################################
# 코스피
# 코스닥
# 각종 지수 
# 

###자동설치################################################################################
# 클릭시 자동 다운
# 자동 실행 

###뉴스################################################################################
# 뉴스 웹크로링
# 검색어시 자동 뉴스 수집 


###문서 변환기################################################################################
# TEXT to pdf
# IMAGE to pdf
# ppT to PDF
# 한글 to pdf
# 워드 to pdf
# pdf to image
# os 모듈, 오피스 모듈
# openCV
# 끌어다 넣기 
# 


###2. 메모장################################################################################



#### 검색결과 파일리스트 박스 만들기
#### 더블클릭시 자동으로 불러오기 


class Tab_text():

    def __init__(self,page):
        self.page = page
   

    def click_search():

        global txt_path
        global label_result,label_result2,name_txt
        global load_files
        global save_path 
        global listbox     

        try:
            save_path = os.path.diranme(txt_path)
        except:
            save_path
        search = name_txt.get()
        file_name = save_path + "/" + "*.txt"
        dir=glob.glob(file_name)
        #label_result.configure(text="")
        #label_result2.configure(text="")  
        count = 0
        listbox.delete(0,END)
        for i,files in enumerate(dir):
            name= os.path.basename(files)
            #file = save_path + "/" + files
            #print("출력",files)
            
            text_txt = open(files,'r')
            print("출력", name)
            while True:     
             line = text_txt.readline()
             if line.find(search) >= 0:
                #label_result.configure(text=name)
                load_files = files
                #label_result2.configure(text=line)
                listbox.insert(END, name)
                #print(count , name)
                count = count + 1
                print(count)
                break
            # else:
            #    label_result.configure(text="결과: 없음!")                
               
        text_txt.close()

    def select(event):
        global Listbox
        global frame1
        global list_retrun
        global txt_path, load_scr        
        global frame1          
        global load_files 
        global save_path      

        select = listbox.curselection()
        list_retrun = listbox.get(select)
        load_scr.delete("1.0","end")  
        file = save_path + "/" + list_retrun
        text_txt = open(file,'r')
        while True:     
             line = text_txt.readline()
             load_scr.insert('1.0', line)  
             if not line:                   
                break     
        text_txt.close()

    def click_1():

        global label_text
        global txt_path
        global save_file
        global save_path      
        txt_path = tk.filedialog.askdirectory()
        label_text.configure(text=txt_path)
        save_txt = open(save_file,'w')               
        save_txt.write(txt_path)          
        save_txt.close
        

    def auto_save():
        #tem 디렉토리 만들기 추가
        #if문     

        global scr1, scr2, scr3, scr4
        global frame
        global txt_path      
        global auto_path          
        #text_scr1 = text_scr2 = text_scr3 = text_scr4 = []
        text_scr1 = scr1.get("1.0", 'end')
        text_scr2 = scr2.get("1.0", 'end')
        text_scr3 = scr3.get("1.0", 'end')
        text_scr4 = scr4.get("1.0", 'end')                    
        txt_save1 = auto_path +  "메모장1.txt"
        txt_save2 = auto_path +  "메모장2.txt"
        txt_save3 = auto_path +  "메모장3.txt"
        txt_save4 = auto_path +  "메모장4.txt"
        text1=len(text_scr1)
        text2=len(text_scr2)
        text3=len(text_scr3)
        text4=len(text_scr4)    
        if text1 >= 3:
            f = open(txt_save1,'w')
            f.write(text_scr1)
            f.close

        if text2 >= 3:
            f = open(txt_save2,'w')
            f.write(text_scr2)
            f.close
             
        if text3 >= 3:
            f = open(txt_save3,'w')
            f.write(text_scr3)
            f.close
             
        if text4 >= 3:
            f = open(txt_save4,'w')
            f.write(text_scr4)
            f.close   
        
        frame.after(10000, Tab_text.auto_save)

    def delete1():
        global auto_path   
        try:
         os.remove(auto_path + "메모장1.txt")
        except:
         pass

    def delete2():
        global auto_path   
        try:
         os.remove(auto_path + "메모장2.txt")
        except:
         pass

    def delete3():
        global auto_path   
        try:
         os.remove(auto_path + "메모장3.txt")
        except:
         pass

    def delete4():
        global auto_path   
        try:
         os.remove(auto_path + "메모장4.txt")
        except:
         pass
        #10초마다 임시저장소에 저장 V
        #메모장을 켰을때 자동적으로 임시저장소의 텍스트 파일을 읽어옴.
        #디렉토리에 텍스트 파일이 없을 경우, 그냥 빈공간으로 실행.
        #
        #불러오기는 텍스트 목록을 더블클릭시 자동으로 불러옴

    def click_save1():

        global frame
        global scr1, scr2, scr3, scr4
        global txt_path
        global txt_name0, txt_name1, txt_name2, txt_name3
        global save_path     
        global auto_path          
        today = date.today()
        now = datetime.now()
        time_name = str(today.year) + "_"+ str(today.month) + "_"+ str(today.day) + "_" + str(now.strftime('%H시%M분%S초'))
        text_scr1 = scr1.get("1.0", 'end')

        name=txt_name0.get()
        txt_save = txt_path+"\\"+str(time_name)+"_"+name+".txt"
        text1=len(text_scr1)
        if text1 >= 3:
              f = open(txt_save,'w')
              f.write(text_scr1)
              f.close
        scr1.delete("1.0","end")
        txt_name0.configure(text=" ")
        Tab_text.delete1()

    def click_save2():

        global frame
        global scr1, scr2, scr3, scr4
        global txt_name0, txt_name1, txt_name2, txt_name3
        global save_path      
        today = date.today()
        now = datetime.now()
        time_name = str(today.year) + "_"+ str(today.month) + "_"+ str(today.day) + "_" + str(now.strftime('%H시%M분%S초'))
        text_scr2 = scr2.get("1.0", 'end')
    
        name=txt_name1.get()
        txt_save = txt_path+"\\"+str(time_name)+"_"+name+".txt"
        text2=len(text_scr2)
        if text2 >= 3:
            f = open(txt_save,'w')
            f.write(text_scr2)
            f.close
        scr2.delete("1.0","end")
        txt_name1.configure(text=" ")
        Tab_text.delete2()

    def click_save3():

        global frame
        global scr1, scr2, scr3, scr4
        global txt_path
        global txt_name0, txt_name1, txt_name2, txt_name3
        global save_path        
        today = date.today()
        now = datetime.now()
        time_name = str(today.year) + "_"+ str(today.month) + "_"+ str(today.day) + "_" + str(now.strftime('%H시%M분%S초'))        
        text_scr3 = scr3.get("1.0", 'end')
 
        name=txt_name2.get()
        txt_save = txt_path+"\\"+str(time_name)+"_"+name+".txt"
        text3=len(text_scr3)
        if text3 >= 3:
            f = open(txt_save,'w')
            f.write(text_scr3)
            f.close
        scr3.delete("1.0","end")
        txt_name2.configure(text=" ")
        Tab_text.delete3()

    def click_save4():

        global frame
        global scr1, scr2, scr3, scr4
        global txt_path
        global txt_name0, txt_name1, txt_name2, txt_name3
        global save_path        
        today = date.today()
        now = datetime.now()
        time_name = str(today.year) + "_"+ str(today.month) + "_"+ str(today.day) + "_" + str(now.strftime('%H시%M분%S초'))        
        text_scr4 = scr4.get("1.0", 'end')

        name=txt_name3.get()
        txt_save = txt_path+"\\"+str(time_name)+"_"+name+".txt"
        text4=len(text_scr4)
        if text4 >= 3:
            f = open(txt_save,'w')
            f.write(text_scr4)
            f.close
        scr4.delete("1.0","end")
        txt_name3.configure(text=" ")
        Tab_text.delete4()
          
    def action(self):

        global label_text
        global save_file
        global txt_path
        global frame, frame1
        global label_result,label_result2, name_txt,load_scr
        global txt_name0, txt_name1, txt_name2, txt_name3
        global save_path
        global listbox
        global auto_path
        try: 
           os.mkdir("c:\\tmp_config")
        except:
           pass

        save_file = "c:\\tmp_config\\save_txt.txt"

        save_txt = open(save_file,'r')
        while True:     
            line_s = save_txt.readline()
            if len(line_s) >= 3:
                save_path = line_s
                txt_path = line_s
        
            elif len(line_s) == 0:                    
                save_path = "C:\\Users\\yhb\\내 드라이브\\7. 메모장"
            if not line_s:    
                break    
        save_txt.close
        
        frame0 = tk.Frame(self.page, relief="solid")
        frame0.grid(column=0, row=0,sticky="w")
 
        frame1 = tk.Frame(self.page, relief="solid")
        frame1.grid(column=0, row=1,sticky="w")
        ## 텍스트 리스트 
 
        frame2 = tk.Frame(self.page, relief="solid")
        frame2.grid(column=0, row=2,sticky="w")
        ## 텍스트 리스트 
        
        scrol_w = 47
        scrol_h = 14
        #scr = scrolledtext.ScrolledText(self.page, width=scrol_w,height=scrol_h, wrap=tk.WORD)
        #scr.grid(column=0,row=3)

        action1 = ttk.Button(frame0, text="경로지정", command=Tab_text.click_1)
        action1.grid(column=0, row=0,sticky="w")                     

        action2 = ttk.Button(frame0, text="텍스트 검색", command=Tab_text.click_search)
        action2.grid(column=0, row=1,sticky="w")   

        #action2 = ttk.Button(frame0, text="텍스트 검색", command=Tab_text.click_search)
        #action2.grid(column=0, row=1,sticky="w")    
    
        name = tk.StringVar() 
        name_txt = ttk.Entry(frame0, width=34, textvariable=name)
        name_txt.grid(column=1, row=1)

        #label_result = ttk.Label(frame0, text='', font=("돋음", 10))
        #label_result.grid(column=1, row=2, sticky="w")

        #label_result2 = ttk.Label(frame0, text='', font=("돋음", 10))
        #label_result2.grid(column=1, row=3, sticky="w")

        ####리스트 박스 시작
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side="right", fill="y")
        listbox = Listbox(frame1, selectmode="extended", width=47,height=10,relief="solid",yscrollcommand=scrollbar.set)
        listbox.pack(side="left", fill="both")
        scrollbar.config(command=listbox.yview)

        load_action = ttk.Button(frame2, text="불러오기")
        load_action.grid(column=0, row=1,sticky="w")

        load_scr = scrolledtext.ScrolledText(frame2, width=scrol_w,height=17, wrap=tk.WORD)
        load_scr.grid(column=0,row=2,columnspan=60)
        load_scr.configure(background="Black",foreground="White")  

        # Binding double click with left mouse
        # button with go function
        listbox.bind('<Double-1>', Tab_text.select)
        listbox.pack()

        k = ["메모장 1 닫기", 
            "메모장 2 닫기",
            "메모장 3 닫기",
            "메모장 4 닫기",

        ]

        for i, text_k in enumerate(k): 
            global scr1, scr2, scr3, scr4
            num = i + 3
            frame = "frame" + str(i+3)
            label = "label" + str(i+3)
            frame = tk.Frame(self.page, relief="solid")
            frame.grid(column=0, row=num, sticky="w")
            saveaction = "saveaction" + str(i)
            if i == 0:
                label = ttk.Label(frame,relief="flat", text= "파일명 입력:", font=("돋음", 10),width=11)
                label.grid(column=1, row=1)
                name = tk.StringVar() 
                txt_name0 = ttk.Entry(frame, width=23, textvariable=name)
                txt_name0.grid(column=2, row=1)
                scr1 = scrolledtext.ScrolledText(frame, width=scrol_w,height=scrol_h, wrap=tk.WORD, font=("돋음", 10))
                scr1.grid(column=0,row=2,columnspan=60)
                scr1.configure(background="Black",foreground="White")                        
                saveaction = ttk.Button(frame, text=text_k, command=Tab_text.click_save1)
                saveaction.grid(column=0, row=1,ipady=0)
            elif i == 1:
                label = ttk.Label(frame,relief="flat", text= "파일명 입력:", font=("돋음", 10),width=11)
                label.grid(column=1, row=1)                
                name = tk.StringVar() 
                txt_name1 = ttk.Entry(frame, width=23, textvariable=name)
                txt_name1.grid(column=2, row=1)                
                scr2 = scrolledtext.ScrolledText(frame, width=scrol_w,height=scrol_h, wrap=tk.WORD, font=("돋음", 10))
                scr2.grid(column=0,row=2,columnspan=60)
                scr2.configure(background="Black",foreground="White")                      
                saveaction = ttk.Button(frame, text=text_k, command=Tab_text.click_save2)
                saveaction.grid(column=0, row=1,ipady=0)    
            elif i == 2:
                label = ttk.Label(frame,relief="flat", text= "파일명 입력:", font=("돋음", 10),width=11)
                label.grid(column=1, row=1)                
                name = tk.StringVar() 
                txt_name2 = ttk.Entry(frame, width=23, textvariable=name)
                txt_name2.grid(column=2, row=1)                
                scr3 = scrolledtext.ScrolledText(frame, width=scrol_w,height=scrol_h, wrap=tk.WORD, font=("돋음", 10))
                scr3.grid(column=0,row=2,columnspan=60)
                scr3.configure(background="Black",foreground="White")                    
                saveaction = ttk.Button(frame, text=text_k, command=Tab_text.click_save3)
                saveaction.grid(column=0, row=1,ipady=0)          
            elif i == 3:
                label = ttk.Label(frame,relief="flat", text= "파일명 입력:", font=("돋음", 10),width=11)
                label.grid(column=1, row=1)                
                name = tk.StringVar() 
                txt_name3 = ttk.Entry(frame, width=23, textvariable=name)
                txt_name3.grid(column=2, row=1)                
                scr4 = scrolledtext.ScrolledText(frame, width=scrol_w,height=scrol_h, wrap=tk.WORD, font=("돋음", 10))
                scr4.grid(column=0,row=2,columnspan=60)
                scr4.configure(background="Black",foreground="White")                
                saveaction = ttk.Button(frame, text=text_k, command=Tab_text.click_save4)
                saveaction.grid(column=0, row=1,ipady=0)
        auto_path = "C:\\Users\\yhb\\내 드라이브\\7. 메모장\\temp\\"            
        auto_file1 = auto_path + "메모장1.txt"
        auto_file2 = auto_path + "메모장2.txt"
        auto_file3 = auto_path + "메모장3.txt"
        auto_file4 = auto_path + "메모장4.txt"

        try:
            text_txt = open(auto_file1,'r')
            while True:     
             line = text_txt.readline()
             scr1.insert('1.0', line)  
             if not line:                   
                break           
            text_txt.close()    
        except:
            pass 
           
        
        try:
            text_txt = open(auto_file2,'r')
            while True:     
             line = text_txt.readline()
             scr2.insert('1.0', line)  
             if not line:                   
                break           
            text_txt.close()    
        except:
            pass 

        try:
            text_txt = open(auto_file3,'r')
            while True:     
             line = text_txt.readline()
             scr3.insert('1.0', line)  
             if not line:                   
                break           
            text_txt.close()    
        except:
            pass 
         

        try:
            text_txt = open(auto_file4,'r')
            while True:     
             line = text_txt.readline()
             scr4.insert('1.0', line)  
             if not line:                   
                break           
            text_txt.close()    
        except:
            pass 
                                       
               
        Tab_text.auto_save()
        label_text = ttk.Label(frame0, text=txt_path, font=("돋음", 10))
        label_text.grid(column=1, row=0,sticky="w")

###2. 유튜브################################################################################
# 2. 유튜트 web brower - 검색창 검색 최대 20개까지 썸내일 표시, 클릭시 재생 및 주소 복사
# 웹크로링, pyauto
# 3. 유튜브 즐겨찾기 
# 유튜브 플레이어

class Tab_youtube():

    def __init__(self,page):
        self.page = page
        
   # def mp3_player():
  #      sound = pyglet.media.load(
#
 #       )

    def mp3_search():
        global path 
        global name_mp3
        global listbox_mp3, listbox_mp4 

        try:
            save = path
            print (save)
        except:
            save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"

        search = name_mp3.get()

        if search == "":
            file_name = save + "/" + "*.mp3"
        else: 
            file_name = save + "/" + "*"+search+"*"+".mp3"
        print(file_name)
        dir=glob.glob(file_name)
        print(dir)
        #label_result.configure(text="")
        #label_result2.configure(text="")  

        listbox_mp3.delete(0,END)
        for i,files in enumerate(dir):
            name= os.path.basename(files)
            #file = save_path + "/" + files
            #print("출력",files)
            listbox_mp3.insert(END, name)
            # else:
            #    label_result.configure(text="결과: 없음!")    
            #  
    def mp4_search():
        global path 
        global name_mp3
        global listbox_mp3, listbox_mp4 

        try:
            save = path
            print (save)
        except:
            save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"

        search = name_mp4.get()

        if search == "":
            file_name = save + "/" + "*.mp4"
        else: 
            file_name = save + "/" + "*"+search+"*"+".mp4"
        print(file_name)
        dir=glob.glob(file_name)
        print(dir)
        #label_result.configure(text="")
        #label_result2.configure(text="")  

        listbox_mp4.delete(0,END)
        for i,files in enumerate(dir):
            name= os.path.basename(files)
            #file = save_path + "/" + files
            #print("출력",files)
            listbox_mp4.insert(END, name)
            # else:
            #    label_result.configure(text="결과: 없음!")    
            #  
    def mp3_next():
        global path
        global listbox_mp3
        global mp3
        global index
        try:
             save = path 
        except:
             save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"

        #file_name = save + "/" + "*.mp4"
        #list= listbox_mp3.get()
        #print("출력", list)
        #load_scr.delete("1.0","end")  
        #print(select)

        location = save + "/" + "*.mp3"
        dir=[]
        dir=glob.glob(location)
        try:
            if len(dir)-1 == int(index):
                index = 0
            else:
                index = int(index) + 1    
            next_player=dir[int(index)]
            mixer.init()
            try: 
             mp3.stop()
            except:
             pass

            mp3 = mixer.Sound(next_player)
            mp3.play(+1)  
        except:
            index = 0
            next_player=dir[0]
            mixer.init()
            try: 
             mp3.stop()
            except:
             pass

            mp3 = mixer.Sound(next_player)
            mp3.play(+1)  

            #  
    def mp3_pre():
        global path
        global listbox_mp3
        global mp3
        global index
        try:
             save = path 
        except:
             save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"

        #file_name = save + "/" + "*.mp4"
        #list= listbox_mp3.get()
        #print("출력", list)
        #load_scr.delete("1.0","end")  
        #print(select)

        location = save + "/" + "*.mp3"
        dir=[]
        dir=glob.glob(location)
        if int(index) < 0:
            index = len(dir)-1
        else:
            index = int(index) - 1    
        next_player=dir[int(index)]
        print(next_player)

        mixer.init()
        try: 
            mp3.stop()
        except:
            pass

        mp3 = mixer.Sound(next_player)
        mp3.play(+1)  

    def mp3_player(event):
        global path
        global listbox_mp3
        global mp3
        global index
        try:
             save = path 
        except:
             save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"
        select = listbox_mp3.curselection()
        index = listbox_mp3.curselection()[0]
        list= listbox_mp3.get(select)
        #load_scr.delete("1.0","end")  
        #print(select)
        location = save+"\\"+list
        #print (location)
        mixer.init()
        try: 
            mp3.stop()
        except:
            pass
        mp3 = mixer.Sound(location)
        mp3.play(-1)

    def mp3_replay():
        global mp3
        try:
            mp3.play(-1)
        except:     
             pass 
    def mp3_quit():
        global mp3
        try:
            mp3.stop()
        except:     
             pass 
       
    def mp3_re():
        global mp3
        try:        
            mp3.play(-1)
        except:     
             pass 
    def click_mp4():
     svae = ""
    def click_1():

        global name_entered1
        global label_pt
        global path

        path = tk.filedialog.askdirectory()
        label_pt.configure(text=path)

    def click_2():
        # MP3 다운로드 
        # mp4형태지만 영상 없이 소리만 있는 파일 다운로드
        #mp4에서 mp3로 변환
        global action1, action2, action3
        global name_entered1, label_mp3
        global path

        save_location = ""
        yt_url = name_entered1.get()  
        try:
             save = path 
        except:
             save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"

        base_dir = "C:\\tmp"

        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.mkdir("C:\\tmp")

        YouTube(yt_url).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(base_dir)
        mp4 = glob.glob("C:\\tmp\\*.mp4")
        mp3 = os.path.basename(mp4[0].replace('.mp4', ".mp3"))
        #mp3로 변환된 파일명     
        mp4_clip = VideoFileClip(os.path.join(base_dir,mp4[0]))
        mp4_clip.audio.write_audiofile(os.path.join(save,mp3))

        mp4_clip.close()
        shutil.rmtree(base_dir)
        label_mp3.configure(text="다운완료-!")

    def click_3(): 
        # MP4 다운로드 
        global action1, action2, action3
        global name_entered1, label_mp4
        global path
        
        save_location = ""
        yt_url = name_entered1.get()
        #print(path)  
        try:
            save = path 
        except:
            save = "C:\\Users\\yhb\\내 드라이브\\6. 다운"

        YouTube(yt_url).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(save)
        print("완료!")
        label_mp4.configure(text="다운완료-!")

    def action(self):

        global action1, action2, action3
        global name_entered1, label_mp3, label_mp4
        global label_pt 
        global name_mp3, name_mp4
        global listbox_mp3, listbox_mp4
        global mp3
        frame0 = tk.Frame(self.page, relief="solid")
        frame0.grid(column=0, row=0,sticky="w")

        frame1 = tk.Frame(self.page, relief="solid")
        frame1.grid(column=0, row=1,sticky="w")

        frame11 = tk.Frame(self.page, relief="solid")
        frame11.grid(column=0, row=2,sticky="w")

        frame_mp3 = tk.Frame(self.page, relief="solid")
        frame_mp3.grid(column=0, row=3,sticky="w")

        frame2 = tk.Frame(self.page, relief="solid")
        frame2.grid(column=0, row=4,sticky="w")

        frame_mp4 = tk.Frame(self.page, relief="solid")
        frame_mp4.grid(column=0, row=5,sticky="w")

        #scr = scrolledtext.ScrolledText(self.page, width=scrol_w,height=scrol_h, wrap=tk.WORD)
        #scr.grid(column=0,row=3)

        mp3 = ttk.Button(frame1, text="MP3 검색", command=Tab_youtube.mp3_search)
        mp3.grid(column=0, row=0,sticky="w")    

        name = tk.StringVar() 
        name_mp3 = ttk.Entry(frame1, width=34, textvariable=name)
        name_mp3.grid(column=1, row=0,sticky="w")

        mp3 = ttk.Button(frame11, text="MP3 재생", command=Tab_youtube.mp3_replay)
        mp3.grid(column=0, row=1,sticky="w")    

        mp3 = ttk.Button(frame11, text="MP3 정지", command=Tab_youtube.mp3_quit)
        mp3.grid(column=1, row=1,sticky="w")    

        mp3 = ttk.Button(frame11, text="이전곡", command=Tab_youtube.mp3_pre)
        mp3.grid(column=2, row=1,sticky="w")            

        mp3 = ttk.Button(frame11, text="다음곡", command=Tab_youtube.mp3_next)
        mp3.grid(column=3, row=1,sticky="w")  

        scrollbar_mp3 = Scrollbar(frame_mp3)
        scrollbar_mp3.pack(side="right", fill="y")

        listbox_mp3 = Listbox(frame_mp3, selectmode="extended", width=47,height=36,relief="solid",yscrollcommand=scrollbar_mp3.set)
        listbox_mp3.pack(side="left", fill="both")
        scrollbar_mp3.config(command=listbox_mp3.yview)

        # Binding double click with left mouse
        # button with go function
        listbox_mp3.bind('<Double-1>', Tab_youtube.mp3_player)
        listbox_mp3.pack()

        mp4 = ttk.Button(frame2, text="MP4 검색", command=Tab_youtube.mp4_search)
        mp4.grid(column=0, row=0,sticky="w")   

        name = tk.StringVar() 
        name_mp4 = ttk.Entry(frame2, width=34, textvariable=name)
        name_mp4.grid(column=1, row=0)

        scrollbar_mp4 = Scrollbar(frame_mp4)
        scrollbar_mp4.pack(side="right", fill="y")

        listbox_mp4 = Listbox(frame_mp4, selectmode="extended", width=47,height=36,relief="solid",yscrollcommand=scrollbar_mp4.set)
        listbox_mp4.pack(side="left", fill="both")
        scrollbar_mp4.config(command=listbox_mp4.yview)
        
        # Binding double click with left mouse
        # button with go function
        listbox_mp4.bind('<Double-1>', Tab_youtube.click_2)
        listbox_mp4.pack()

        j = ["URL주소 : "]
        for i, text_j in enumerate(j): 
            num = i 
            i = str(i+1)
            label = "label" + i
            label = ttk.Label(frame0,relief="raise", text= text_j, font=("돋음", 10),width=10)
            label.grid(column=0, row=num)

        label_pt = ttk.Label(frame0 , text='C:/Users/yhb/내 드라이브/6. 다운', font=("돋음", 10))
        label_pt.grid(column=1, row=1, sticky="w")

        label_mp3 = ttk.Label(frame0 , text="", font=("돋음", 10))
        label_mp3.grid(column=1, row=2)

        label_mp4 = ttk.Label(frame0 , text="", font=("돋음", 10))
        label_mp4.grid(column=1, row=3)

        name = tk.StringVar() 
        name_entered1 = ttk.Entry(frame0 , width=30, textvariable=name)
        name_entered1.grid(column=1, row=0)
            
        action1 = ttk.Button(frame0, text="경로지정", command=Tab_youtube.click_1)
        action1.grid(column=0, row=1)  
          
        action2 = ttk.Button(frame0, text="MP3 다운", command=Tab_youtube.click_2)
        action2.grid(column=0, row=2)     
        
        action3 = ttk.Button(frame0, text="MP4 다운", command=Tab_youtube.click_3)
        action3.grid(column=0, row=3) 
           
        #frame= HtmlFrame.HtmlFrame(self.page)
        #frame.load_website(https://www.youtube.com/)
        #frame.pack(fill="both", expand=True)
        #유튜브 웹페이지 띄우기   
        #self.action_3(action)

        #click = self.click_4(name_entered)
        #action4 = ttk.Button(self.page, text="삭제", command=click)
        #action4.grid(column=2, row=3)  
        cef.Initialize(settings={"windowless_rendering_enabled": True})    
                        
        parent_window_handle = 0
        window_info = cef.WindowInfo()
        window_info.SetAsOffscreen(parent_window_handle)
        browser = cef.CreateBrowserSync(window_info=window_info,
                                url="http://www.youtube.com")

###########################################################################################

def main():

    win = tk.Tk()
    #tkinter 클래스에서 TK()란 인스턴스를 생성한다.
    #그리고 win이란 변수에 클래스 인스턴스 할당한다.

    win.title("")

    win.geometry("350x1360+3080+000")
    #GUI 사이즈 크기
    #너비X높이+x좌표,y좌표
    win.resizable(False,False)
    # GUI 사이즈 크기 변경 막음

    tabControl = ttk.Notebook(win,takefocus=True)

    j = ["위젯 멀티 메모장", 
    "유튜브 다운 플레이어", 
    ]

    for i, menu_name in enumerate(j) :
        i = str(i)
        tab = "tab"+ i
        tab = ttk.Frame(tabControl)
        #
        tabControl.add(tab, text = menu_name)
        #
        tab_page = "tab_page"+ i
        
        #if tab_page == "tab_page0":
           #주식 메뉴_0
        #   Menu0 = Tab_Stock(tab)
        #   Menu0.action()   
        if tab_page == "tab_page0":
           #youtube 메뉴_1
           Menu0 = Tab_text(tab)
           Menu0.action()               
        elif tab_page == "tab_page1":
           #youtube 메뉴_2
           Menu1 = Tab_youtube(tab)
           Menu1.action()
    
    tabControl.pack(expand=1, fill="both")
   

    win.mainloop()
    #mainloop 메서드 호출하여 윈도우의 이벤트 순환문을 시작

###########################################################################################

if __name__ == '__main__': 
    main()