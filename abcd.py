from tkinter import*
from tkinter.ttk import Combobox # giao diện sịn sò hơn
import tkinter as tk 
from tkinter import ttk 
import os #  tương tác với hệ thống tệp
import pandas as pd # được sử dụng để xử lý và phân tích dữ liệu
import numpy as np # hữu ích cho các phép tính số học và xử lý mảng.
import matplotlib # dùng để tạo các biểu đồ và hình ảnh minh họa
import matplotlib.pyplot as plt #tạo các biểu đồ và hình ảnh trực quan.
import seaborn as sns #giúp tạo các biểu đồ thống kê đẹp mắt và dễ sử dụng.
import warnings
from tkinter import filedialog, messagebox, ttk
warnings.filterwarnings('ignore') #Bỏ qua các cảnh báo để đầu ra gọn gàng hơn
df = pd.read_csv("heart.csv", sep=',')
sns.set(style="whitegrid")



def cp():

    cp_count = df['cp'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = cp_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = cp_count.values  # Lấy số lượng
    fig, ax = plt.subplots()

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    cp_labels = {
        0: 'Loại 0 :Không đau ngực',
        1: 'Loại 1 :Đau thắt ngực điển hình',
        2: 'Loại 2 :Đau thắt ngực không điển hình',
        3: 'Loại 3 :Không đau ngực nhưng có triệu chứng'
    }
    # Thêm chú thích
    ax.legend(wedges, [cp_labels[int(lang)] for lang in langs], 
          title="Loại đau ngực", 
          loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

# Đặt tiêu đề
    plt.title('Tỉ lệ bệnh nhân theo loại đau ngực (cp)',fontsize= 16)
    plt.show()

def sex():
    sex_count = df['sex'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = sex_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = sex_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    sex_labels = {
        0: '0 : nữ',
        1: '1: nam',
    }
    # Thêm chú thích
    ax.legend(wedges, [sex_labels[int(lang)] for lang in langs], 
          title="Tỉ lệ bênh nhân theo giới tính", 
          loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

    plt.show()
def fbs():
    fbs_count = df['fbs'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = fbs_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = fbs_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([-0.2, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    fbs_labels = {
        0: 'Loại 0 :Đường huyết khi đói bình thường (thấp hơn 120 mg/dL)',
        1: 'Loại 1 :Đường huyết khi đói cao (lớn hơn hoặc bằng 120 mg/dL)',
    }
    # Thêm chú thích
    ax.legend(wedges, [fbs_labels[int(lang)] for lang in langs], 
          title="Lượng đường trong máu khi đói", 
          loc="center left", 
          bbox_to_anchor=(1, 0,-0.4, 0.5))  # Vị trí chú thích

    plt.show()
def restecg():
    restecg_count = df['restecg'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = restecg_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = restecg_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    restecg_labels = {
        0: 'Loại 0 :Không có sóng ST',
        1: 'Loại 1 :Sóng ST bình thường)',
        2: 'Loại 2 :Có sóng ST bất thường'
    }
    # Thêm chú thích
    ax.legend(wedges, [restecg_labels[int(lang)] for lang in langs], 
            title="Điện tâm đồ khi nghỉ ngơi", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

    plt.show()
def exng():
    exng_count = df['exng'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = exng_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = exng_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    exng_labels = {
        0: 'Loại 0 :Không có đau ngực khi gắng sức',
        1: 'Loại 1 :Có đau ngực khi gắng sức',
        
    }
    # Thêm chú thích
    ax.legend(wedges, [exng_labels[int(lang)] for lang in langs], 
            title="Đau ngực do gắng sức", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

    plt.show()

def slp():
    slp_count = df['slp'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = slp_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = slp_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([-0.2, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    slp_labels = {
        0: '0 : Độ dốc của đoạn ST âm tính',
        1: '1 :Độ dốc của đoạn ST bằng phẳng',
        2: '2 :Độ dốc của đoạn ST dương tính'
    }
    # Thêm chú thích
    ax.legend(wedges, [slp_labels[int(lang)] for lang in langs], 
            title="Độ dốc của đoạn ST cực đại trong bài kiểm tra gắng sức", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

    plt.show()
def caa():
    caa_count = df['caa'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = caa_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = caa_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([-0.2, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    h1_labels = {
        0: '0: mạch máu không bị tổn thương',
        1: '1: có tổn thương nhẹ',
        2: '2: có tổn thương',
        3: '3: có tổn thương nghiêm trọng',
        4: '4:tổn thương rất nghiêm trọng'
    }
    # Thêm chú thích
    ax.legend(wedges, [h1_labels[int(lang)] for lang in langs], 
            title="Độ dốc của đoạn ST cực đại trong bài kiểm tra gắng sức", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích
    plt.show()
def thall():
    thall_count = df['thall'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = thall_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = thall_count.values  # Lấy số lượng
    fig = plt.figure()
    ax = fig.add_axes([-0.2, 0, 1, 1])
    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    thall_labels = {
        0: '0 : Không xác định',
        1: '1 : Bình thường ',
        2: '2 :Khiếm khuyết cố định',
        3: '3 :khiếm khuyết cố thể phục hồi'
    }
    # Thêm chú thích
    ax.legend(wedges, [thall_labels[int(lang)] for lang in langs], 
            title="Độ dốc của đoạn ST cực đại trong bài kiểm tra gắng sức", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

    plt.show()
def output():
    output_count = df['output'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = output_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = output_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig = plt.figure()
    ax = fig.add_axes([-0.2, 0, 1, 1])

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    output_labels = {
        0: '0 : Bệnh nhân không mắc bệnh tim.',
        1: '1: Bệnh nhân mắc bệnh tim.',
        
    }
    # Thêm chú thích
    ax.legend(wedges, [output_labels[int(lang)] for lang in langs], 
            title="Kết quả phân loại", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

    plt.show()
def age():
    plt.figure(figsize=(8, 6))
    sns.histplot(df['age'], bins=20, color='skyblue', alpha=0.7,kde=True)
    plt.title("biểu đô phân phối độ tuổi của người bệnh")
    plt.xlabel("Tuổi")
    plt.ylabel("Số người")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
def trtbps():
    # 2. Phân phối huyết áp (trtbps)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['trtbps'], bins=20, color='lightcoral', alpha=0.7,kde=True)
    plt.title("biểu đồ phân phối huyết áp bệnh nhân (mmHg)")
    plt.xlabel("huyết áp nghỉ ngơi(mmHg)")
    plt.ylabel("Count")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
def chol():
    # 3. Phân phối cholesterol (chol)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['chol'], bins=20, color='lightgreen', alpha=0.7,kde=True)
    plt.title("Biểu đồ phân phối Cholesterol")
    plt.xlabel("Cholesterol(mg/dL)")
    plt.ylabel("số người")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
def thalachh():
    # 4. Phân phối nhịp tim tối đa (thalachh)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['thalachh'], bins=20, color='orange', alpha=0.7,kde=True)
    plt.title("Phân phối nhịp tim tối đa (thalachh)")
    plt.xlabel("thalachh")
    plt.ylabel("Count")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
def oldpeak():
    # 5. Phân phối oldpeak
    plt.figure(figsize=(8, 6))
    sns.histplot(df['oldpeak'], bins=20, color='purple', alpha=0.7,kde=True)
    plt.title("Phân phối oldpeak")
    plt.xlabel("oldpeak")
    plt.ylabel("Count")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

#giao dien
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

Du_Lieu = None
treeview = None

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
frame = tk.Frame(root, bg='#f0ddd5')
frame.place(x=400, y=30, width=930, height=660)

#Tạo hàm mở file csv
def Open_Folder(): #Mở thư mục
    global Du_Lieu, treeview
    #Mở hộp thoại để chọn tệp (người dùng chỉ có thể chọn file có đuôi csv)
    file_path = filedialog.askopenfilename(
        title='Chọn file csv',
        filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
    if not file_path:
        return
    try:
        Du_Lieu = pd.read_csv(file_path) #Đọc tệp csv vào biến Du_Lieu theo dạng DataFrame
    except Exception as e:
        messagebox.showerror('Lỗi',f'không thể đọc file {e}')
        return
    Create_Treeview()

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

#Hàm để thêm dữ liệu mới nhập vào Treeview
def Update_Treeview():
    global treeview
    #Xóa các mục hiện tại trong Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    for _, row in Du_Lieu.iterrows():
        treeview.insert('', 'end', values=list(row))

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
        messagebox.showinfo('Thông báo','Dữ liệu đã được nhập thành công!')
    Create_Data_Window = Toplevel(root)
    Create_Data_Window.title('Tạo dòng dữ liệu mới')
    Create_Data_Window.geometry('400x500')

    for i, column in enumerate(Du_Lieu.columns):
        Label(Create_Data_Window, text=column, font=('Arial', 10)).grid(row=i, column=0, padx=10, pady=5)
        entry = Entry(Create_Data_Window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        Name_Key[column] = entry
    Button(Create_Data_Window, text='Lưu dữ liệu', command=Save_Create_Data).grid(row=len(Du_Lieu.columns), column=0, columnspan=2, pady=20)



Button(crud_entry, text="Chọn file muốn đọc", bd=0,font="arial 12", bg="pink", cursor="hand2", width=37, command=Open_Folder).place(x=20, y=0)
Button(crud_entry, text="Tạo dữ liệu mới cho file",font="arial 12", bd=0, bg="pink", cursor="hand2", width=37, command=Create_Data).place(x=20, y=30)
Button(crud_entry, text="Chỉnh sửa dữ liệu",font="arial 12", bd=0, bg="pink", cursor="hand2", width=37).place(x=20, y=60)
Button(crud_entry, text="Khôi phục dữ liệu",font="arial 12", bd=0, bg="pink", cursor="hand2", width=37).place(x=20, y=90)
Button(crud_entry, text="Xóa dữ liệu",font="arial 12", bd=0, bg="pink", cursor="hand2", width=37).place(x=20, y=120)

Button(crud_entry, text="Tỉ lệ bệnh nhân theo loại đau ngực (cp)", font="arial 14", bd=0, bg=framebg, width=30, command=cp).place(x=20,y=170)
Button(crud_entry, text="Tỉ lệ bênh nhân theo giới tính", font="arial 14", bd=0, bg=framebg, width=30,command=sex).place(x=20, y=210)
Button(crud_entry, text="Lượng đường trong máu khi đói", font="arial 14", bd=0, bg=framebg, width=30,command=fbs).place(x=20, y=250)
Button(crud_entry, text="Điện tâm đồ khi nghỉ ngơi", font="arial 14", bd=0, bg=framebg, width=30,command=restecg).place(x=20, y=290)
Button(crud_entry, text="Đau ngực do gắng sức", font="arial 14", bd=0, bg=framebg, width=30,command=exng).place(x=20, y=330)
Button(crud_entry, text="Độ dốc trong bài kiểm tra gắng sức", font="arial 14", bd=0, bg=framebg, width=30,command=fbs).place(x=20, y=370)
Button(crud_entry, text="?", font="arial 14", bd=0, bg=framebg, width=30,command=caa).place(x=20, y=410)
Button(crud_entry, text="?", font="arial 14", bd=0, bg=framebg, width=30,command=thall).place(x=20, y=450)
Button(crud_entry, text="Phân phối tuổi", font="arial 14", bd=0, bg=framebg, width=30,command=age).place(x=20, y=490)
Button(crud_entry, text="Phân phối oldpeak", font="arial 14", bd=0, bg=framebg, width=30,command=trtbps).place(x=20, y=530)
Button(crud_entry, text="Phân phối cholesterol", font="arial 14", bd=0, bg=framebg, width=30,command=chol).place(x=20, y=570)
Button(crud_entry, text="Phân phối cholesterol", font="arial 14", bd=0, bg=framebg, width=30,command=thalachh).place(x=20, y=610)
Button(crud_entry, text="Phân phối huyết áp", font="arial 14", bd=0, bg=framebg, width=30,command=oldpeak).place(x=20, y=650)
Button(crud_entry, text="Kết quả phân loại", font="arial 14", bd=0, bg=framebg, width=30,command=output).place(x=20, y=690)
root.mainloop()
