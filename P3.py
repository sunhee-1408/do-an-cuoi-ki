from tkinter import *
Icon = Tk()
Icon.title('Thông tin')
Icon.geometry('850x600')
#Icon chú thích
IcTT = PhotoImage(file = 'C:/Users/hi/Documents/Đồ án/Information.png')
Icon.iconphoto(False, IcTT)

#Tiêu đề của phần chú thích
Label(Icon,text='Information Related To Heart Attack Analysis & Prediction Dataset', font ='robot 19 bold').pack(padx = 20, pady = 20)

#Chú thích
Label(Icon,text='age - Age of the person',font='arial 11').place(x=20,y=100)
Label(Icon,text='sex - Gender of person',font='arial 11').place(x=20,y=130)
Label(Icon,text='cp - Chest Pain type chest pain type',font='arial 11').place(x=20,y=160)
Label(Icon,text='trtbps - resting blood pressure (in mm Hg)',font='arial 11').place(x=20,y=190)
Label(Icon,text='chol - cholestoral in mg/dl fetched via BMI sensor',font='arial 11').place(x=20,y=220)
Label(Icon,text='fbs - fasting blood suger > 120 mg/dl (1 = true; 0 = false)',font='arial 11').place(x=20,y=250)
Label(Icon,text='restecg - resting electrocardiographic results',font='arial 11').place(x=20,y=280)
Label(Icon,text='thalachh - maximum heart rate achieved',font='arial 11').place(x=20,y=310)
Label(Icon,text='exng - exercise included agina (1 = yes; 0 = no)',font='arial 11').place(x=20,y=340)
Label(Icon,text='old peak - Previous peak',font='arial 11').place(x=20,y=370)

Icon.mainloop()
