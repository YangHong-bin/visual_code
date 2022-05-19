#-*- coding:utf-8 -*-
#_*_coding:cp949_*_

import os, glob,sys
from pdf2image.pdf2image import convert_from_path
import win32com.client as win32
import win32gui
import pdf2image 
import shutil, time
import stat

def remove_readonly(func, path, excinfo): 
    os.chmod(path, stat.S_IWRITE) 
    func(path)

hwp_dir = 'C:/Users\yhb\AppData\Local\Temp\gen_py'
if os.path.exists(hwp_dir):
     shutil.rmtree(hwp_dir)

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwnd = win32gui.FindWindow(None, 'Noname 1 - HWP')


base_dir = os.path.dirname(os.path.abspath( __file__ ))    
img_dir = 'C:/Users/yhb/내 드라이브/1. 동기화/IMAGE'
D_pdf_dir = 'C:/Users/yhb/내 드라이브/1. 동기화/PDF'
 #if os.path.exists(img_dir) == False: # 저장 경로 없으면 만들기
 # os.makedirs(img_dir)    
hwp_dir =glob.glob('C:/Users/yhb/내 드라이브/1. 동기화/*.hwp')
 # convert_from_path를 이용해 pdf파일를 이미지형태로 불러온다.
 #for pdf in pdf_dir:
 # images = convert_from_path(pdf)
 # images는 여러 페이지로 구성되어 있어 아래와 같이 각각의 페이지(이미지)를 jpg로 저장한다.  
 #  for i, image in enumerate(images):
 #    image.save("c:\Users\yhb\Google Drive\\1. 동기화\이미지"+".jpg", "JPEG") 

if os.path.exists(img_dir):
        shutil.rmtree(img_dir, ignore_errors=False, onerror=remove_readonly)
        os.makedirs(img_dir)
else:
        os.makedirs(img_dir)

if os.path.exists(D_pdf_dir):
        shutil.rmtree(D_pdf_dir, ignore_errors=False, onerror=remove_readonly)

        os.makedirs(D_pdf_dir)
else:
        os.makedirs(D_pdf_dir)



for i in hwp_dir:
    hwp.Open(i)
    hwp.SaveAs(os.path.join(D_pdf_dir, os.path.basename(i.replace('.hwp', "")))+".pdf", "PDF")
    hwp.Quit()


    
pdf_dir =glob.glob('C:\\Users\\yhb\\내 드라이브\\1. 동기화\\PDF\\*.pdf')
print (pdf_dir)

for pdf in pdf_dir: 
   print ("출력:", pdf)
   pages = convert_from_path(pdf, dpi=300)
   for i, page in enumerate(pages): 
    page.save(os.path.join(img_dir, os.path.basename(pdf.replace('.pdf', "_")))+str(i)+".jpg", "JPEG")
    #save 위치 경로를 잡을 때를 주의하자.
print("완료!")

