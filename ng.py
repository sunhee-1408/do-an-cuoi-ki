from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk

# Cài đặt màu nền
background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

# Tạo cửa sổ chính
root = Tk()
root.title("HEART ATTACK PREDICTION SYSTEM")
root.geometry("1400x730+60+80")
root.resizable(False, False)
root.configure(bg=background)

# Phần các nút CRUD và ô nhập liệu ở bên phải
def create_button_frame():
    crud_frame = Frame(root, width=200, height=300, bg=framebg, relief=RIDGE, bd=2)
    crud_frame.place(x=1200, y=100)

    Label(crud_frame, text="Information", bg=framebg, fg="white", font=("Arial", 12, "bold"))\
        .place(x=30, y=10)

    Button(crud_frame, text="Registration", bd=0, bg="#ff6f61", fg="white", font=("Arial", 10, "bold"), cursor="hand2", width=15).place(x=20, y=50)
    Entry(crud_frame, width=20, font=("Arial", 10)).place(x=20, y=80)

    Button(crud_frame, text="Date", bd=0, bg="#4caf50", fg="white", font=("Arial", 10, "bold"), cursor="hand2", width=15).place(x=20, y=120)
    Entry(crud_frame, width=20, font=("Arial", 10)).place(x=20, y=150)

    Button(crud_frame, text="Patient Name", bd=0, bg="#2196f3", fg="white", font=("Arial", 10, "bold"), cursor="hand2", width=15).place(x=20, y=190)
    Entry(crud_frame, width=20, font=("Arial", 10)).place(x=20, y=220)

    Button(crud_frame, text="Birth Year", bd=0, bg="#f44336", fg="white", font=("Arial", 10, "bold"), cursor="hand2", width=15).place(x=20, y=260)
    Entry(crud_frame, width=20, font=("Arial", 10)).place(x=20, y=290)

# Gọi hàm tạo nút CRUD và ô nhập liệu
create_button_frame()

# Chạy vòng lặp chính
root.mainloop()