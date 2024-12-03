from tkinter import *
from datetime import date # thư viện làm việc với ngày và thời gian
from tkinter.ttk import Combobox # giao diện sịn sò hơn
import datetime # làm 
import tkinter as tk 
from tkinter import ttk 
import os #  tương tác với hệ thống tệp 

import matplotlib # thuư viện về biểu đồ

matplotlib.use("TkAgg") # thiết lập giao diện
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # dùng để tích hợp biểu đồ của Matplotlib vào giao diện Tkinter

from matplotlib.figure import Figure # làm khung biểu đồ
import numpy as np # thư viên tính toán
import matplotlib.pyplot as plt # vẽ biểu dò trực tiép

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

#----------------------------------------------------------------------------------------------------------------------------------------------


root = tk.Tk()
root.title("HEART ATTACK  PREDICTION SYSTEM")  # tieu de
root.geometry("1400x730+60+80") #kich thuoc 
root.resizable(False,False) # ko cho chinh sua kich thuoc 
root.configure(bg=background)  # Thay đổi màu nền của cửa sổ chính

#----------------------------------------------------------------------------------------------------------------------------------------------
 
#icon 1
imade_icon = PhotoImage(file="images/images(1).png")
root.iconphoto(False,imade_icon)

# header 2
logo =PhotoImage(file="")
logo_resized = logo.zoom(5, 1)
myimage=Label(image=logo_resized,bg=background)
myimage.place(x=0,y=0)

#3
heading_entry= Frame(root,width=800,height=190,bg="#df2d4b")
heading_entry.place(x=600,y=20)

Label(heading_entry, text = "Registration No.", font="ariel 13" ,bg="#df2d4b", fg=framefg).place(x=30,y=0)
Label(heading_entry,text ="Age" ,font="ariel 13" ,bg="#df2d4b", fg=framefg).place(x=30,y=90)

entry_image= PhotoImage(file="")
entry_image2= PhotoImage(file="")

Label(heading_entry,image=entry_image2, bg="#df2d4b").place(x=20,y=30)
Label(heading_entry,image=entry_image2, bg="#df2d4b").place(x=20,y=120)

registration=IntVar()
reg_entry =Entry(heading_entry,textvariable=registration,width=30,font="arial 15",bg="#0e5363",fg="white",bd=0)
reg_entry.place(x=30,y=45)

age=IntVar()
age_entry= Entry(heading_entry,textvariable=age,width=20, font="arial 20", bg="#ededed",fg="#222222",bd=0)
age_entry.place(x=30,y=130)

#---------------------------------------body-------------------------------------
detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
detail_entry.place(x=30,y=450)

#--------------radio button ------------
Label(detail_entry,text="sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(detail_entry,text="fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(detail_entry,text="exng:",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)

def selection():
    if gen.get() == 1:
        gender= 1
        return(gender)
        print(gender)
    elif gen.get() == 2:
        gender=0
        return(gender)
        print(gender)
    else:
        print(gender)


def selection2():
    if fbs.get() == 1:
        Fbs= 1
        return(Fbs)
        print(Fbs)
    elif fbs.get() == 2:
        Fbs=0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exng.get() == 1:
        Exng= 1
        return(Exang)
        print(Exng)
    elif exang.get() == 2:
        Exng=0
        return(Exng)
        print(Exng)
    else:
        print(Exng)

gen=IntVar()
r1=Radiobutton(detail_entry,text="male", variable=gen, value=1)
r2=Radiobutton(detail_entry,text="female",variable=gen, value=2)
r1.place(x=43 ,y=10)
r2.place(x=93,y=10)


fbs = IntVar()
r3=Radiobutton(detail_entry,text="True", variable=fbs, value=1)
r4=Radiobutton(detail_entry,text="False",variable=fbs, value=2)
r3.place(x=213 ,y=10)
r4.place(x=263,y=10)


exang=IntVar()
r5=Radiobutton(detail_entry,text="Yes", variable=exang, value=1)
r6=Radiobutton(detail_entry,text="No",variable=exang, value=2)
r5.place(x=387 ,y=10)
r6.place(x=430,y=10)

#---------------------------------combobox-------------

Label(detail_entry,text="cp",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(detail_entry,text="restecg",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(detail_entry,text="slp",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(detail_entry,text="caa",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(detail_entry,text="thall",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)
root.mainloop()
