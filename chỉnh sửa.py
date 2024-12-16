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
row_in_page = 27
current_page = 0
Backup_Data = None
#Hàm tạo Treeview
def Create_Treeview():
    global treeview

    #Xóa các phần Treeview cũ
    for widget in frame.winfo_children():
        widget.destroy()

    #Tạo nút cuộn lên xuống
    scroll_up_down = Scrollbar(frame, orient='vertical')
    scroll_up_down.pack(side='right', fill='y')

    #Tạo nút cuộn trái phải
    scroll_left_right = Scrollbar(frame, orient='horizontal')
    scroll_left_right.pack(side='bottom',fill='x')

    #Gắn dữ liệu và cuộn vào Treeview
    treeview = ttk.Treeview(frame, column=list(Du_Lieu.columns), show='headings'
                        , yscrollcommand=scroll_up_down.set, xscroll=scroll_left_right.set)
    treeview.pack(fill=BOTH, expand=True)

    #Cấu hình cột trong Treeview
    for cot in Du_Lieu.columns:
        treeview.heading(cot, text=cot)
        treeview.column(cot, width=120, anchor='center')

    #Kết nối cuộn vào Treeview
    scroll_left_right.config(command=treeview.xview)
    scroll_up_down.config(command=treeview.yview)
    # Thêm dữ liệu từ DataFrame vào Treeview
    for _, row in Du_Lieu.iterrows():
        treeview.insert('', 'end', values=list(row))

#Tạo frame chứa Treeview
frame = tk.Frame(root, bg=background)
frame.place(x=240, y=30, width=930, height=600)

#Tạo hàm mở file csv
def Open_Folder(): #Mở thư mục
    global Du_Lieu, treeview, current_page
    #Mở hộp thoại để chọn tệp (người dùng chỉ có thể chọn file có đuôi csv)
    file_path = filedialog.askopenfilename(
        title='Chọn file csv',
        filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
    if not file_path:
        return
    try:
        Du_Lieu = pd.read_csv(file_path) #Đọc tệp csv vào biến Du_Lieu theo dạng DataFrame
        current_page = 0
        Create_Treeview()
        Update_Page_Treeview()
        Create_Page_Button()
    except Exception as e:
        messagebox.showerror('Lỗi',f'không thể đọc file {e}')
        return
    Create_Treeview()

#Tạo frame chứa các nút trang
Frame_Button = tk.Frame(root, bg=background)

#Hàm cập nhật Treeview theo trang
def Update_Page_Treeview():
    global treeview, current_page
    # Tính tổng số trang
    all_page = (len(Du_Lieu) + row_in_page - 1) // row_in_page
    if current_page >= all_page:
        current_page = max(0, all_page - 1)  # Giới hạn current_page trong phạm vi hợp lệ

    # Tính hàng bắt đầu và kết thúc
    start_row = current_page * row_in_page
    end_row = min(start_row + row_in_page, len(Du_Lieu))

    # Xóa dữ liệu hiện tại của Treeview
    for item in treeview.get_children():
        treeview.delete(item)

    # Chèn dữ liệu tương ứng với trang hiện tại
    for _, row in Du_Lieu.iloc[start_row:end_row].iterrows():
        treeview.insert('', 'end', values=list(row))

#Hàm chuyển trang
def Go_To_Page(page):
    global current_page
    all_page = (len(Du_Lieu) + row_in_page - 1) // row_in_page
    if 0 <= page < all_page:
        current_page = page
        Update_Page_Treeview()

#Hàm tạo các nút trang (phân trang)
def Create_Page_Button():
    global all_page

    for widget in Frame_Button.winfo_children():
        widget.destroy()

    all_page = (len(Du_Lieu) + row_in_page - 1) // row_in_page #Tính số trang

    Frame_Button.place(x=250, y=630, width=700, height=100)
    cot_count = 0
    hang_count = 0
    for i in range(all_page):
        Button_Page = Button(Frame_Button, text=f'Trang {i+1}', bd=1, bg=background, cursor='hand2',
                             width=8, command=lambda page=i: Go_To_Page(page))  # Truyền tham số page
        Button_Page.grid(row=hang_count, column=cot_count, padx=5, pady=5)
        cot_count += 1
        if cot_count >= 8:  # Sau 8 cột chuyển sang hàng mới
            cot_count = 0
            hang_count += 1
    Button(Frame_Button, text='Tất cả các trang', bd=1, bg=background, cursor='hand2', width=30, command=All_Page).grid(row=hang_count, column=cot_count, columnspan=8, padx=5, pady=5)

#Tạo hàm trở về tất cả các trang 
def All_Page():
    global current_page
    # Xóa dữ liệu cũ trong Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    # Hiển thị toàn bộ dữ liệu trong Treeview mà không phân trang
    for _, row in Du_Lieu.iterrows():
        treeview.insert('', 'end', values=list(row))
    # Đặt lại trạng thái trang hiện tại về ban đầu (không có phân trang)
    current_page = -1

#Tạo hàm kiểm tra dữ liệu người dùng nhập vào
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
def Open_Folder():
    global Du_Lieu, Backup_Data, treeview

    file_path = filedialog.askopenfilename(
        title='Chọn file csv',
        filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
    if not file_path:
        return
    try:
        Du_Lieu = pd.read_csv(file_path)
        Backup_Data = Du_Lieu.copy()  # Lưu trữ bản sao dữ liệu ban đầu
    except Exception as e:
        messagebox.showerror('Lỗi', f'Không thể đọc file: {e}')
        return
    Create_Treeview()

#Hàm để thêm dữ liệu mới nhập vào Treeview
def Update_Treeview():
    global treeview
    #Xóa các mục hiện tại trong Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    for _, row in Du_Lieu.iterrows():
        treeview.insert('', 'end', values=list(row))    
    Create_Page_Button()


#Hàm để tạo dòng mới
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
                    return #Dừng hàm ngay lập tức nếu gặp lỗi
        
        #Chuyền phần dictionary ở trên thành DataFrame
        new_row_DF = pd.DataFrame([new_row])
        global Du_Lieu #Dùng biến toàn cục Du_Lieu
        Du_Lieu = pd.concat([Du_Lieu, new_row_DF], ignore_index = True) #Nối dòng mới vào dữ liệu
        Update_Treeview()
        Create_Page_Button()
        Update_Page_Treeview()
        messagebox.showinfo('Thông báo','Dữ liệu đã được nhập thành công!')
        Create_Data_Window.destroy() #Tự đóng cửa sổ sau khi lưu dữ liệu
    Create_Data_Window = Toplevel(root)
    Create_Data_Window.title('Tạo dòng dữ liệu mới')
    Create_Data_Window.geometry('400x500')

    for i, column in enumerate(Du_Lieu.columns):
        Label(Create_Data_Window, text=column, font=('Arial', 10)).grid(row=i, column=0, padx=10, pady=5)
        entry = Entry(Create_Data_Window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        Name_Key[column] = entry
    Button(Create_Data_Window, text='Lưu dữ liệu', command=Save_Create_Data).grid(row=len(Du_Lieu.columns), column=0, columnspan=2, pady=20)
# Hàm tìm kiếm dữ liệu
def Search_Data():
    if Du_Lieu is None:
        messagebox.showerror('Lỗi', 'Vui lòng mở file trước khi tìm kiếm')
        return

    def Apply_Search():
        nonlocal search_window
        column = column_combobox.get()
        search_value = search_entry.get()

        if not search_value:
            messagebox.showerror('Lỗi', 'Vui lòng nhập giá trị cần tìm')
            return

        try:
            if column == "Tất cả các cột":
                # Tìm kiếm trên toàn bộ bảng
                filtered_data = Du_Lieu[
                    Du_Lieu.apply(lambda row: row.astype(str).str.contains(search_value, case=False, na=False).any(), axis=1)
                ]
            else:
                # Tìm kiếm trên một cột cụ thể
                filtered_data = Du_Lieu[Du_Lieu[column].astype(str).str.contains(search_value, case=False, na=False)]

            if filtered_data.empty:
                messagebox.showinfo('Thông báo', 'Không tìm thấy dữ liệu phù hợp')
                return

            # Hiển thị dữ liệu tìm kiếm trên Treeview
            for item in treeview.get_children():
                treeview.delete(item)
            for _, row in filtered_data.iterrows():
                treeview.insert('', 'end', values=list(row))
            
            search_window.destroy()  # Đóng cửa sổ sau khi áp dụng tìm kiếm
        except Exception as e:
            messagebox.showerror('Lỗi', f'Lỗi khi tìm kiếm dữ liệu: {e}')

    # Cửa sổ nhập thông tin tìm kiếm
    search_window = Toplevel(root)
    search_window.title('Tìm kiếm dữ liệu')
    search_window.geometry('300x250')

    Label(search_window, text='Chọn cột:', font=('Arial', 10)).pack(pady=10)
    column_combobox = Combobox(
        search_window, values=["Tất cả các cột"] + list(Du_Lieu.columns), state='readonly'
    )
    column_combobox.current(0)  # Chọn "Tất cả các cột" mặc định
    column_combobox.pack(pady=5)

    Label(search_window, text='Nhập giá trị tìm kiếm:', font=('Arial', 10)).pack(pady=10)
    search_entry = Entry(search_window)
    search_entry.pack(pady=5)

    Button(search_window, text='Tìm kiếm', command=Apply_Search).pack(pady=20)
def Restore_Data():
    global Du_Lieu, Backup_Data

    if Backup_Data is None:
        messagebox.showerror('Lỗi', 'Không có dữ liệu nào để khôi phục!')
        return

    Du_Lieu = Backup_Data.copy()
    Update_Treeview()
    messagebox.showinfo('Thông báo', 'Dữ liệu đã được khôi phục về trạng thái ban đầu!')



# Thêm nút tìm kiếm dữ liệu vào giao diện
Button(crud_entry, text="Tìm kiếm dữ liệu", bd=1, bg=background, cursor="hand2", width=19, command=Search_Data).place(x=15, y=45)
Button(crud_entry, text="Chọn file để đọc", bd=1, bg=background, cursor="hand2", width=19, command=Open_Folder).place(x=15, y=10)
Button(crud_entry, text="Tạo dòng mới", bd=1, bg=background, cursor="hand2", width=19, command=Create_Data).place(x=15, y= 80)
Button(crud_entry, text="Khôi phục dữ liệu", bd=1, bg=background, cursor="hand2", width=19, command=Restore_Data).place(x=15, y=115)
Button(crud_entry, text="Xóa dữ liệu", bd=1, bg=background, cursor="hand2", width=19).place(x=15, y=150)
Button(crud_entry, text='Chỉnh sửa dữ liệu', bd=1, bg=background, cursor='hand2', width=19).place(x=15, y=185)

root.mainloop()