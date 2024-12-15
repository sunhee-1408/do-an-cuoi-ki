from tkinter import*
from datetime import date # thư viện làm việc với ngày và thời gian
from tkinter.ttk import Combobox # giao diện xịn sò hơn
import tkinter as tk 
import os #  tương tác với hệ thống tệp
import pandas as pd
from tkinter import filedialog, messagebox, ttk
import numpy as np

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

#Khỏi tạo cửa sổ giao diện
root=Tk() #Tạo cửa sổ chính
root.title("HEART ATTACK PREDICTION SYSTEM")  #Tiêu đề
root.geometry("1150x1200") #Kích thước
root.resizable(True, True) # Không chỉnh sửa được kích thước
root.configure(bg=background) #Thay đổi nền của cửa sổ chính

crud_entry=Frame(root,width=170, height=220)
crud_entry.place(x=25,y=30)

#Biến toàn cục để lưu trữ dữ liệu và Treeview
Du_Lieu = None
treeview = None

#Hàm tạo Treeview
def Create_Treeview():
    global treeview


    for widget in frame.winfo_children():
        widget.destroy()

    #Tạo nút cuộn lên xuống
    scroll_up_down = Scrollbar(frame, orient='vertical')
    scroll_up_down.pack(side='right', fill='y')

    #Tạo nút cuộn trái phải
    scroll_left_right = Scrollbar(frame, orient='horizontal')
    scroll_left_right.pack(side='bottom',fill='x')

 
    treeview = ttk.Treeview(frame, column=list(Du_Lieu.columns), show='headings'
                        , yscrollcommand=scroll_up_down.set, xscroll=scroll_left_right.set)
    treeview.pack(fill=BOTH, expand=True)


    for cot in Du_Lieu.columns:
        treeview.heading(cot, text=cot)
        treeview.column(cot, width=120, anchor='center')


    scroll_left_right.config(command=treeview.xview)
    scroll_up_down.config(command=treeview.yview)

    for _, row in Du_Lieu.iterrows():
        treeview.insert('', 'end', values=list(row))

#Tạo frame chứa Treeview
frame = tk.Frame(root, bg='white')
frame.place(x=240, y=30, width=930, height=670)

#Tạo hàm mở file csv
def Open_Folder(): 
    global Du_Lieu, treeview

    file_path = filedialog.askopenfilename(
        title='Chọn file csv',
        filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
    if not file_path:
        return
    try:
        Du_Lieu = pd.read_csv(file_path)
    except Exception as e:
        messagebox.showerror('Lỗi',f'không thể đọc file {e}')
        return
    Create_Treeview()

#Hàm ktra
def Check(prompt):
    while True:
        user_input = input(prompt)
        if user_input == '':
            return np.nan
        try:
            value = float(user_input)
            return value
        except ValueError:
            print('Giá trị người dùng nhập không hợp lệ (nhập 1 số hoặc để trống)')


def Update_Treeview():
    global treeview
 
    for item in treeview.get_children():
        treeview.delete(item)
    for _, row in Du_Lieu.iterrows():
        treeview.insert('', 'end', values=list(row))


def Create_Data():
    global Du_Lieu
    if Du_Lieu is None:
        messagebox.showerror('Lỗi', 'Vui lòng mở file trước khi thêm dữ liệu mới')
        return
    
    Name_Key = {}

    def Save_Create_Data():
        new_row = {}
        for column, entry in Name_Key.items():
            value = entry.get()
            if value == '':
                new_row[column] = np.nan
            else:
                try:
                    new_row[column] = float(value)
                except ValueError:
                    messagebox.showerror('Lỗi', f'Dữ liệu nhập cho {column} không hợp lệ, vui lòng nhập lại!')
                    return 
        
 
        new_row_DF = pd.DataFrame([new_row])
        global Du_Lieu 
        Du_Lieu = pd.concat([Du_Lieu, new_row_DF], ignore_index = True) 
        Update_Treeview()
        messagebox.showinfo('Thông báo','Dữ liệu đã được nhập thành công!')
    Create_Data_Window = Toplevel(root)
    Create_Data_Window.title('Tạo dòng dữ liệu mới')
    Create_Data_Window.geometry('400x500')

    for i, column in enumerate(Du_Lieu.columns):
        Label(Create_Data_Window, text=column, font=('Arial', 12)).grid(row=i, column=0, padx=10, pady=10)
        entry = Entry(Create_Data_Window)
        entry.grid(row=i, column=1, padx=10, pady=10)
        Name_Key[column] = entry
    Button(Create_Data_Window, text='Lưu dữ liệu', command=Save_Create_Data).grid(row=len(Du_Lieu.columns), column=0, columnspan=2, pady=20)






Button(crud_entry, text="Chọn file để đọc", bd=1, bg=background, cursor="hand2", width=19, command=Open_Folder).place(x=15, y=20)
Button(crud_entry, text="Tạo dòng mới", bd=1, bg=background, cursor="hand2", width=19, command=Create_Data).place(x=15, y= 60)
Button(crud_entry, text="Khôi phục dữ liệu", bd=1, bg=background, cursor="hand2", width=19).place(x=15, y=100)
Button(crud_entry, text="Xóa dữ liệu", bd=1, bg=background, cursor="hand2", width=19).place(x=15, y=140)
Button(crud_entry, text='Chỉnh sửa dữ liệu', bd=1, bg=background, cursor='hand2', width=19).place(x=15, y=180)
root.mainloop()
