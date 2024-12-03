from tkinter import *
from datetime import date # thư viện làm việc với ngày và thời gian
from tkinter.ttk import Combobox # giao diện sịn sò hơn
import datetime # làm 
import tkinter as tk 
from tkinter import ttk 
import os #  tương tác với hệ thống tệp 
from tkinter import messagebox
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

###Phân tích
def analysis():
    name = Name.get()
    D1 = date.get()
    today = datetime.date.today()
    A = today.year-DOB.get()

    try:
        B = selection()
    except:
        messagebox.showerror('Missing','Please select gender!')
        return
     
    try:
        F = selection2()
    except:
        messagebox.showerror('Missing','Please select fbs!')
        return 
    
    try:
        I = selection3()
    except:
        messagebox.showerror('Missing','Please select exang!')
        return
    
    try:
        C = int(selection4())
    except:
        messagebox.showerror('Missing','Please select cp!')
        return
    
    try:
        G = int(restecg_combobox.get())
    except:
        messagebox.showerror('Missing','Please select restecg!')
        return 
    
    try:
        K = int(selection5())
    except:
        messagebox.showerror('Missing','Please select slope!')
        return
    
    try:
        L = int(ca_combobox.get())
    except:
        messagebox.showerror('Missing','Please select ca!')
        return
    
    try:
        M = int(thall_combobox.get())
    except:
        messagebox.showerror('Missing','Please select thal!')
        return 

    try:
        D = int(trtbps.get())
        E = int(chol.get())
        H = int(thalachh.get())
        J = int(oldpeak.get())
    except:
        messagebox.showerror('Missing data','Few missing data entry!')
        return 
    #Kiểm tra có hoạt động không
    print('A is age: ',A)
    print('B is gender: ',B)
    print('C is cp: ',C)
    print('D is trestbps: ',D)
    print('E is chol: ',E)
    print('F is fbs: ',F)
    print('G is restcg: ',G)
    print('H is thalach: ',H)
    print('I is Exang: ',I)
    print('J is oldpeak: ',J)
    print('K is slop: ',K)
    print('L is ca: ',L)
    print('M is thal: ',M)

#Chú thích (Nút Info)
def Info():
    Icon = Toplevel(root)
    Icon.title('Thông tin')
    Icon.geometry('850x600')
    #Icon chú thích
    IcTT = PhotoImage(file = '')
    Icon.iconphoto(False, IcTT)

    #Tiêu đề của phần chú
    Label(Icon,text='Information Related To Heart Attack Analysis & Prediction Dataset', font ='robot 19 bold').pack(padx = 20, pady = 20)

    #Chú thích
    Label(Icon,text='age - Age of the person',font='arial 11').place(x=20,y=100)
    Label(Icon,text='sex - Gender of person',font='arial 11').place(x=20,y=130)
    Label(Icon,text='cp - Chest Pain type chest pain type',font='arial 11').place(x=20,y=160)
    Label(Icon,text='trestbps - resting blood pressure (in mm Hg)',font='arial 11').place(x=20,y=190)
    Label(Icon,text='chol - cholestoral in mg/dl fetched via BMI sensor',font='arial 11').place(x=20,y=220)
    Label(Icon,text='fbs - fasting blood suger > 120 mg/dl (1 = true; 0 = false)',font='arial 11').place(x=20,y=250)
    Label(Icon,text='restecg - resting electrocardiographic results',font='arial 11').place(x=20,y=280)
    Label(Icon,text='thalachh - maximum heart rate achieved',font='arial 11').place(x=20,y=310)
    Label(Icon,text='exang - exercise included agina (1 = yes; 0 = no)',font='arial 11').place(x=20,y=340)
    Label(Icon,text='old peak - Previous peak',font='arial 11').place(x=20,y=370)
    Label(Icon,text='slope - the slope of the peak exercise ST segment',font='arial 11').place(x=20,y=400)
    Label(Icon,text='ca - number of major vessels',font='arial 11').place(x=20,y=430)
    Label(Icon,text='thal - 0; 1 = fixed defect; 2 = reversable defect',font='arial 11').place(x=20,y=460)

    Icon.mainloop()

####Nút tắt
def logout():
    root.destroy()

###Nút xóa
def Clear():
    Name.get('')
    DOB.get('')
    trtbps.get('')
    chol.get('')
    thalachh.set('')
    oldpeak.set('')

#icon 1
imade_icon = PhotoImage(file="")
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

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(heading_entry,textvariable=Date,width=15,font='arial 15',bg='#0e5363',fg='white',bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)

Name = StringVar()
name_entry = Entry(heading_entry,textvariable=Name,width=20,font='arial 20',bg='#ededed',fg='#222222',bd=0)
name_entry.place(x=30,y=130)

DOB = IntVar()
dob_entry = Entry(heading_entry,textvariable=DOB,width=20,font='arial 20',bg='#ededed',fg='222222',bd=0)
dob_entry.place(x=450,y=130)

age=IntVar()
age_entry= Entry(heading_entry,textvariable=age,width=20, font="arial 20", bg="#ededed",fg="#222222",bd=0)
age_entry.place(x=30,y=130)

#---------------------------------------body-------------------------------------
detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
detail_entry.place(x=30,y=450)

#--------------radio button ------------
Label(detail_entry,text="sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(detail_entry,text="fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(detail_entry,text="exang:",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)

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
    if exang.get() == 1:
        Exang= 1
        return(Exang)
        print(Exang)
    elif exang.get() == 2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

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


def selection4():
    input=cp_combobox.get()
    if input =="0":
        return(0)
    elif input=="1":
        return (1)
    elif input=="2":
        return(2)
    elif input=="3":
        return(3)
    else:
        print(exang)
    

def selection5():
    input=slp_combobox.get()
    if input =="0":
        return(0)
    elif input=="1":
        return (1)
    elif input=="2":
        return(2)
    else:
        print(exang)

    

##########
cp_combobox=Combobox(detail_entry, values = ['0 = typical angina','1 = atypical angina', '2 = non-anginal pain ', '3 = asympotomaic'], state='r', width=21)
restecg_combobox=Combobox(detail_entry, values = ['0', '1','2'], font ="arial 12", state='r', width=11)
slp_combobox=Combobox(detail_entry, values = ['0 = upsloping','1 = flat ','2 = downloping'], font ="arial 12", state='r', width=12)
ca_combobox=Combobox(detail_entry, values = ['0', '1', '2','3','4'], font ="arial 12", state='r', width=14)
thall_combobox=Combobox(detail_entry, values = ['0','1','2','3'], font ="arial 12", state='r', width=14)


cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=80, y=90)
slp_combobox.place(x=70, y=130)
ca_combobox.place(x=50, y=170)
thall_combobox.place(x=50, y=210)

######## entry_box
Label(detail_entry, text="Smoking:", font ="arial 13", width=7, bg="#dbe0e3", fg="black").place(x=240, y=50)
Label(detail_entry, text="trtbps:", font ="arial 13", width=7, bg=framebg, fg="black").place(x=240, y=90)
Label(detail_entry, text="chol:", font ="arial 13", width=7, bg=framebg, fg="black").place(x=240, y=130)
Label(detail_entry, text="thalachh:", font ="arial 13", width=7, bg=framebg, fg="black").place(x=240, y=170)
Label(detail_entry, text="oldpeak:", font ="arial 13", width=7, bg=framebg, fg="black").place(x=240, y=210)


trtbps= StringVar()
chol= StringVar()
thalachh= StringVar()
oldpeak= StringVar()

trtbps_entry=Entry(detail_entry, textvariable=trtbps, width=10, font ="arial 15", bg="#ededed", fg="#222222", bd=0)
chol_entry=Entry(detail_entry, textvariable=chol, width=10, font ="arial 15", bg="#ededed", fg="#222222", bd=0)
thalachh_entry=Entry(detail_entry, textvariable=thalachh, width=10, font ="arial 15", bg="#ededed", fg="#222222", bd=0)
oldpeak_entry=Entry(detail_entry, textvariable=oldpeak, width=10, font ="arial 15", bg="#ededed", fg="#222222", bd=0)


trtbps_entry.place(x=320, y=90)
chol_entry.place(x=320, y=130)
thalachh_entry.place(x=320, y=170)
oldpeak_entry.place(x=320, y=210)

###############Report ####
square_report_image=PhotoImage(file="")
report_background=Label(image=square_report_image, bg= background)
report_background.place(x=1120, y= 340)

report=Label(root, font="arial 25 bold", bg="white", fg="#8dc36f")
report.place(x=1130, y=610)

#############Graph #####
graph_image=PhotoImage(file="")
Label(image=graph_image).place(x=600, y=270)
Label(image=graph_image).place(x=860, y=270)
Label(image=graph_image).place(x=600, y=500)
Label(image=graph_image).place(x=860, y=500)


######Button 
analysis_button=PhotoImage(file="")
Button(root, image=analysis_button, bd=0, bg=background, cursor= 'hand2',command=analysis).place(x=1130, y=240)
######Info button
info_button = PhotoImage(file ="")
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command=Info).place(x=10,y=240)
#####Save_button
save_button=PhotoImage(file="")
Button(root, image= save_button, bg=background, cursor= 'hand2').place(x=1370, y=250)



####Smoking and Non Smoking
button_mode=True
choice="smoking"

button_mode=True
choice="smoking"
def changemode():
    global button_mode
    global choice
    if button_mode:
        choice="nonsmoking_icon "
        mode.config(image=nonsmoking_icon, activebackground= "white")
        button_mode=False
    else:
        choice="smoking_icon"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode=True
    
    print(choice)

smoking_icon=PhotoImage(file="")
nonsmoking_icon=PhotoImage(file="")

mode=Button(root,image=smoking_icon, bg="#dbe0e3", bd=0, cursor='hand2', command=changemode)
mode.place(x=350, y=495)


############Logout_Button
logout_icon=PhotoImage(file="")
logout_button=Button(root, image=logout_icon, bg="#df2d4b", cursor='hand2', bd=0,command=logout)
logout_button.place(x=1390, y=60)



root.mainloop()
