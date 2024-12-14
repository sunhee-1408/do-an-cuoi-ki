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


crud_entry=Frame(root,width=400, height=800)
crud_entry.place(x=0,y=0)

Button(crud_entry, text="Create", bd=0,font="arial 15", bg="pink", cursor="hand2", width=30).place(x=20, y= 20)
Button(crud_entry, text="Read",font="arial 15", bd=0, bg="pink", cursor="hand2", width=30 ).place(x=20, y=60)
Button(crud_entry, text="Save",font="arial 15", bd=0, bg="pink", cursor="hand2", width=30).place(x=20, y=100)
Button(crud_entry, text="Delete",font="arial 15", bd=0, bg="pink", cursor="hand2", width=30).place(x=20, y=140)

Button(crud_entry, text="AGE", font="arial 14", bd=0, bg=framebg, width=20).place(x=80,y=180)
Button(crud_entry, text="CP", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=220)
Button(crud_entry, text="trtbps", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=260)
Button(crud_entry, text="chol", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=300)
Button(crud_entry, text="fbs", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=340)
Button(crud_entry, text="restecg", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=380)
Button(crud_entry, text="thalachh", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=420)
Button(crud_entry, text="exng", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=460)
Button(crud_entry, text="oldpeak", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=500)
Button(crud_entry, text="slp", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=540)
Button(crud_entry, text="caa", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=580)
Button(crud_entry, text="thall", font="arial 14", bd=0, bg=framebg, width=20).place(x=80, y=620)





root.mainloop()