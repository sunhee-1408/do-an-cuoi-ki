from tkinter import*
from datetime import date # thư viện làm việc với ngày và thời gian
from tkinter.ttk import Combobox # giao diện sịn sò hơn
import tkinter as tk 
from tkinter import ttk 
import os #  tương tác với hệ thống tệp

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"
root=Tk()
root.title("HEART ATTACK  PREDICTION SYSTEM")  #Tiêu đề
root.geometry("1400x730+60+80") #Kích thước
root.resizable(False,False) # Không chỉnh sửa được kích thước
root.configure(bg=background) #Thay đổi nền của cửa sổ chính


crud_entry=Frame(root,width=150, height= 150)
crud_entry.place(x=30,y=10)

Button(crud_entry, text="Create", bd=0, bg=background, cursor="hand2", width=15).place(x=20, y= 20)
Button(crud_entry, text="Read", bd=0, bg=background, cursor="hand2", width=15 ).place(x=20, y=50)
Button(crud_entry, text="Save", bd=0, bg=background, cursor="hand2", width=15).place(x=20, y=80)
Button(crud_entry, text="Delete", bd=0, bg=background, cursor="hand2", width=15).place(x=20, y=110)




detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
detail_entry.place(x=30,y=450)


Label(detail_entry,text="sex", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=10)
Label(detail_entry,text="fbs",font="arial 13",bg=framebg, fg=framefg).place(x=160,y=10)
Label(detail_entry, text="exng", font="arial 13", bg=framebg, fg=framefg).place(x=310, y=10)
Label(detail_entry,text="cp",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(detail_entry,text="restecg",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(detail_entry,text="slp",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(detail_entry,text="caa",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(detail_entry,text="thall",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)
Label(detail_entry,text="trtbps",font="arial 13", bg=framebg, fg=framefg).place(x=260, y=50)
Label(detail_entry,text="chol",font="arial 13", bg=framebg, fg=framefg).place(x=260, y=90)
Label(detail_entry,text="thacllach",font="arial 13", bg=framebg, fg=framefg).place(x=260, y=130)
Label(detail_entry,text="outpeak",font="arial 13",bg=framebg, fg=framefg).place(x=260, y=170)


sex_combobox=Combobox(detail_entry,values=['1-Male','0-Female'],font="arial 12", state='r',width=8)
fbs_combobox=Combobox(detail_entry,values=['1-True','0-False'],font="arial 12", state='r', width=8)
exang_combobox=Combobox(detail_entry,values=['1-Yes','0-No'],font="arial 12", state='r',width=8)
cp_combobox=Combobox(detail_entry, values = ['0', '1', '2', '3'],font="arial 12", state='r', width=8)
restecg_combobox=Combobox(detail_entry, values = ['0', '1'], font ="arial 12", state='r', width=8)
slp_combobox=Combobox(detail_entry, values = ['0', '1', '2'], font ="arial 12", state='r', width=8)
caa_combobox=Combobox(detail_entry, values = ['0', '1', '2','3'], font ="arial 12", state='r', width=8)
thall_combobox=Combobox(detail_entry, values = ['1', '2', '3'], font ="arial 12", state='r', width=8)



trtbps=StringVar()
chol=StringVar()
thallach=StringVar()
outpeak=StringVar()


trtbps_entry=Entry(detail_entry, textvariable=trtbps,width =12, font="arial 15",bg="#ededed", fg="#222222", bd=0)
chol_entry=Entry(detail_entry, textvariable=chol, width=12, font="arial 15", bg="#ededed", fg="#222222", bd=0)
thallach_entry=Entry(detail_entry, textvariable=thallach, width=12, font="arial 15", bg="#ededed", fg="#222222", bd=0)
outpeak_entry=Entry(detail_entry, textvariable=outpeak, width=12, font="arial 15", bg="#ededed", fg="#222222", bd=0)




sex_combobox.place(x=50, y=10)
fbs_combobox.place(x=200, y=10)
exang_combobox.place(x=370,y=10)
cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=80, y=90)
slp_combobox.place(x=50, y=130)
caa_combobox.place(x=50, y=170)
thall_combobox.place(x=50, y=210)  


trtbps_entry.place(x=320, y=50)
chol_entry.place(x=310, y=90)
thallach_entry.place(x=340,y =130)
outpeak_entry.place(x=330, y=170)











root.mainloop()