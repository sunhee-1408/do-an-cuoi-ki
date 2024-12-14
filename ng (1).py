from tkinter import *

# Cài đặt màu nền
background = "#f0ddd5"  # Nền chính
framebg = "#d32f2f"     # Nền khung (đỏ)
framefg = "#fefbfb"     # Màu chữ

# Tạo cửa sổ chính
root = Tk()
root.title("Thông tin")
root.geometry("1300x600+1+1")
root.resizable(False, False)
root.configure(bg=background)

# Phần các thông tin và ô nhập liệu
def create_info_section():
    info_frame = Frame(root, width=0, height=1, bg=framebg, relief=RIDGE, bd=3)
    info_frame.place(x=1, y=1)  # Đặt khung ngang ở giữa cửa sổ

    Label(info_frame, text="Patient Information", bg=framebg, fg="white", 
          font=("Arial", 16, "bold")).pack(pady=10)

    # Các trường dữ liệu (nằm ngang)
    row_frame = Frame(info_frame, bg=framebg)  # Tạo dòng chứa thông tin
    row_frame.pack()

    options = [
        ("Registration", "Enter Registration ID"),
        ("Date", "Enter Date (DD/MM/YYYY)"),
        ("Patient Name", "Enter Name"),
        ("Birth Year", "Enter Birth Year"),
    ]

    for label_text, placeholder in options:
        # Nhãn
        Label(row_frame, text=label_text, bg=framebg, fg="white", 
              font=("Arial", 12, "bold")).pack(side=LEFT, padx=15)
        # Ô nhập liệu
        Entry(row_frame, width=20, font=("Arial", 12), 
              fg="gray").pack(side=LEFT, padx=10)

# Gọi hàm tạo giao diện thông tin
create_info_section()

# Chạy vòng lặp chính
root.mainloop()