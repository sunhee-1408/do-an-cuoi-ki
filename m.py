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
    ax.set_title('Tỉ lệ bệnh nhân theo loại đau ngực (cp)',fontsize= 16)
    plt.show()     
def sex():
    sex_count = df['sex'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = sex_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = sex_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig, ax = plt.subplots()

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
    ax.set_title('Tỉ lệ bênh nhân theo giới tính(sex)',fontsize= 16)
    plt.show()
def fbs():
    fbs_count = df['fbs'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = fbs_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = fbs_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig, ax = plt.subplots()

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
    ax.set_title('Tỉ lệ lượng đường trong máu khi đói(fbs)',fontsize=16 )
    plt.show()
def restecg():
    restecg_count = df['restecg'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = restecg_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = restecg_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig, ax = plt.subplots()

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    restecg_labels = {
        0: 'Loại 0 :Không có sóng ST',
        1: 'Loại 1 :Sóng ST bình thường',
        2: 'Loại 2 :Có sóng ST bất thường'
    }
    # Thêm chú thích
    ax.legend(wedges, [restecg_labels[int(lang)] for lang in langs], 
            title="Điện tâm đồ khi nghỉ ngơi", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích
    ax.set_title('Tỉ lệ điện tâm đồ khi nghỉ ngơi(restecg)',fontsize=16)    
    plt.show()
def exng():
    exng_count = df['exang'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = exng_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = exng_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig,ax = plt.subplots()
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
    ax.set_title('Tỉ lệ đau ngực do gắng sức(exng)',fontsize=16 )
    plt.show()
def slp():
    slp_count = df['slp'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = slp_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = slp_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig, ax = plt.subplots()

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
    ax.set_title('Tỉ lệ độ dốc của đoạn ST cực đại trong bài kiểm tra gắng sức(slp)',fontsize=16 )
    plt.show()
def caa():
    caa_count = df['ca'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = caa_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = caa_count.values  # Lấy số lượng

    # Vẽ biểu đồ
    fig, ax = plt.subplots()


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
            title="Bất thường động mạch vành", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích
    ax.set_title('Tỉ lệ bất thường động mạch vành',fontsize=16 )
    plt.show()
def thall():
    thall_count = df['thal'].value_counts()  # Đếm số lượng từng loại đau ngực
    langs = thall_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
    values = thall_count.values  # Lấy số lượng
    fig, ax = plt.subplots()

    wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

    thall_labels = {
        0: '0 : Không xác định',
        1: '1 : Bình thường ',
        2: '2 :Khiếm khuyết cố định',
        3: '3 :khiếm khuyết cố thể phục hồi'
    }
    # Thêm chú thích
    ax.legend(wedges, [thall_labels[int(lang)] for lang in langs], 
            title="Kết quả chụp quét Thallium", 
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích
    ax.set_title('Tỉ lệ kết quả chụp quét Thallium',fontsize=16 )
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
    plt.title("Biểu đồ phân phối độ tuổi của người bệnh")
    plt.xlabel("Tuổi")
    plt.ylabel("Số người")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
def trtbps():
    # 2. Phân phối huyết áp (trtbps)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['trestbps'], bins=20, color='lightcoral', alpha=0.7,kde=True)
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
    sns.histplot(df['thalach'], bins=20, color='orange', alpha=0.7,kde=True)
    plt.title("Phân phối nhịp tim tối đa (thalachh)")
    plt.xlabel("thalach")
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
framebg = "aqua"
framefg = "#fefbfb"
root=Tk()
root.title("HEART ATTACK  PREDICTION SYSTEM")  #Tiêu đề
root.geometry("1400x730+60+80") #Kích thước
root.resizable(True, True) # Không chỉnh sửa được kích thước
root.configure(bg=background) #Thay đổi nền của cửa sổ chính



crud_entry=Frame(root,width=400, height=800)
crud_entry.place(x=0,y=0)
Backup_Data = None  # Lưu trữ bản sao để khôi phục dữ liệu    
Du_Lieu = None
treeview = None
current_page = 0
row_in_page = 27
#Tạo frame chứa các nút trang
Frame_Button = tk.Frame(root, bg=background)
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
frame.place(x=400, y=0, width=1135, height=600)

#Tạo hàm mở file csv
def Open_Folder(): #Mở thư mục
    global Du_Lieu, treeview, current_page, Backup_Data
    #Mở hộp thoại để chọn tệp (người dùng chỉ có thể chọn file có đuôi csv)
    file_path = filedialog.askopenfilename(
        title='Chọn file csv',
        filetypes=[('CSV files', '*.csv'), ('All files', '*.*')])
    if not file_path:
        return
    try:
        Du_Lieu = pd.read_csv(file_path) #Đọc tệp csv vào biến Du_Lieu theo dạng DataFrame
        Backup_Data = Du_Lieu.copy()
        current_page = 0
        Create_Treeview()
        Update_Page_Treeview()
        Create_Page_Button()
    except Exception as e:
        messagebox.showerror('Lỗi',f'không thể đọc file {e}')
        return
    Create_Treeview()
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

    # Xóa các nút cũ trong Frame_Button
    for widget in Frame_Button.winfo_children():
        widget.destroy()

    # Tính tổng số trang
    if row_in_page <= 0:
        raise ValueError("Số dòng trên mỗi trang (row_in_page) phải lớn hơn 0.")
    all_page = (len(Du_Lieu) + row_in_page - 1) // row_in_page

    # Đặt vị trí Frame_Button
    Frame_Button.place(x=450, y=600, width=1000, height=200)  # Tăng chiều rộng và chiều cao frame
    max_columns = 11  # Giảm số nút trong một hàng
    col_count = 0
    row_count = 0

    # Font chữ trong các nút phân trang
    from tkinter import font
    default_font = font.Font(size=12)

    # Tạo nút cho từng trang
    for i in range(all_page):
        Button(
            Frame_Button,
            text=f'Trang {i+1}',
            bd=1,
            bg='white',
            cursor='hand2',
            width=20, 
            font=default_font, 
            command=lambda page=i: Go_To_Page(page)
        ).grid(row=row_count, column=col_count, padx=5, pady=8) 
        col_count += 1
        if col_count >= max_columns:
            col_count = 0
            row_count += 1

    # Thêm nút "Tất cả các trang"
    Button(
        Frame_Button,
        text='Tất cả các trang',
        bd=2,
        bg='white',
        cursor='hand2',
        width=20,
        font=default_font,
        command=All_Page
    ).grid(row=row_count, column=col_count, columnspan=3, padx=5, pady=8, sticky='nsew')

    # Cấu hình lưới
    for i in range(row_count + 1):
        Frame_Button.grid_rowconfigure(i, weight=1)
    for i in range(max_columns):
        Frame_Button.grid_columnconfigure(i, weight=1)
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
        Update_Page_Treeview()
        Create_Page_Button()
        messagebox.showinfo('Thông báo','Dữ liệu đã được nhập thành công!')
        Create_Data_Window.destroy()
    Create_Data_Window = Toplevel(root)
    Create_Data_Window.title('Tạo dòng dữ liệu mới')
    Create_Data_Window.geometry('400x500')

    for i, column in enumerate(Du_Lieu.columns):
        Label(Create_Data_Window, text=column, font=('Arial', 10)).grid(row=i, column=0, padx=10, pady=5)
        entry = Entry(Create_Data_Window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        Name_Key[column] = entry
    Button(Create_Data_Window, text='Lưu dữ liệu', command=Save_Create_Data).grid(row=len(Du_Lieu.columns), column=0, columnspan=2, pady=20)
def Edit_Data():
    global Du_Lieu, treeview

    if Du_Lieu is None:
        messagebox.showerror('Lỗi', 'Vui lòng mở file trước khi chỉnh sửa dữ liệu')
        return

    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror('Lỗi', 'Vui lòng chọn một dòng để chỉnh sửa')
        return

    selected_index = treeview.index(selected_item[0])

    Edit_Data_Window = Toplevel(root)
    Edit_Data_Window.title('Chỉnh sửa dữ liệu')
    Edit_Data_Window.geometry('400x800')

    Name_Key = {}

    def Save_Edit_Data():
        nonlocal selected_index

        edited_row = {}
        for column, entry in Name_Key.items():
            value = entry.get()
            if value == '':
                edited_row[column] = np.nan
            else:
                try:
                    edited_row[column] = float(value) if value.replace('.', '', 1).isdigit() else value
                except ValueError:
                    messagebox.showerror('Lỗi', f'Dữ liệu nhập cho {column} không hợp lệ, vui lòng nhập lại!')
                    return

        for column in Du_Lieu.columns:
            Du_Lieu.loc[selected_index, column] = edited_row[column]

        Update_Treeview()
        Edit_Data_Window.destroy()
        messagebox.showinfo('Thông báo', 'Dữ liệu đã được chỉnh sửa thành công!')

    for i, column in enumerate(Du_Lieu.columns):
        Label(Edit_Data_Window, text=column, font=('Arial', 12)).grid(row=i, column=0, padx=10, pady=10)
        entry = Entry(Edit_Data_Window)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entry.insert(0, str(Du_Lieu.loc[selected_index, column]))
        Name_Key[column] = entry

    Button(Edit_Data_Window, text='Lưu thay đổi', command=Save_Edit_Data).grid(row=len(Du_Lieu.columns), column=0, columnspan=2, pady=20)
def Delete_Data():
    global Du_Lieu, treeview

    if Du_Lieu is None:
        messagebox.showerror('Lỗi', 'Vui lòng mở file trước khi xóa dữ liệu')
        return

    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror('Lỗi', 'Vui lòng chọn một dòng để xóa')
        return

    confirm = messagebox.askyesno('Xác nhận', 'Bạn có chắc chắn muốn xóa dòng dữ liệu này?')
    if not confirm:
        return

    selected_index = treeview.index(selected_item[0])
    Du_Lieu = Du_Lieu.drop(selected_index).reset_index(drop=True)
    Update_Treeview()
    messagebox.showinfo('Thông báo', 'Dữ liệu đã được xóa thành công!')
# Hàm tìm kiếm dữ liệu
def Search_Data():
    # Kiểm tra nếu dữ liệu (Du_Lieu) chưa được mở, hiển thị thông báo lỗi và kết thúc hàm.
    if Du_Lieu is None:
        messagebox.showerror('Lỗi', 'Vui lòng mở file trước khi tìm kiếm')
        return

    def Apply_Search():
        # Lấy thông tin cột được chọn và giá trị cần tìm từ giao diện.
        nonlocal search_window
        column = column_combobox.get()  # Lấy cột được chọn từ combobox
        search_value = search_entry.get()  # Lấy giá trị tìm kiếm từ ô nhập liệu

        # Nếu người dùng không nhập giá trị tìm kiếm, hiển thị lỗi.
        if not search_value:
            messagebox.showerror('Lỗi', 'Vui lòng nhập giá trị cần tìm')
            return

        try:
            # Kiểm tra nếu tìm kiếm trên toàn bộ bảng
            if column == "Tất cả các cột":
                # Lọc dữ liệu: Kiểm tra từng dòng xem có chứa giá trị tìm kiếm (bất kể chữ hoa/thường)
                filtered_data = Du_Lieu[
                    Du_Lieu.apply(lambda row: row.astype(str).str.contains(search_value, case=False, na=False).any(), axis=1)
                ]
            else:
                # Tìm kiếm trên một cột cụ thể, lọc dữ liệu thỏa mãn điều kiện
                filtered_data = Du_Lieu[Du_Lieu[column].astype(str).str.contains(search_value, case=False, na=False)]

            # Nếu không tìm thấy kết quả phù hợp, hiển thị thông báo
            if filtered_data.empty:
                messagebox.showinfo('Thông báo', 'Không tìm thấy dữ liệu phù hợp')
                return

            # Xóa toàn bộ dữ liệu hiện có trên Treeview (bảng hiển thị dữ liệu)
            for item in treeview.get_children():
                treeview.delete(item)

            # Thêm dữ liệu đã lọc vào Treeview
            for _, row in filtered_data.iterrows():
                treeview.insert('', 'end', values=list(row))

            # Đóng cửa sổ tìm kiếm sau khi áp dụng
            search_window.destroy()
        except Exception as e:
            # Nếu có lỗi trong quá trình tìm kiếm, hiển thị thông báo lỗi
            messagebox.showerror('Lỗi', f'Lỗi khi tìm kiếm dữ liệu: {e}')

    # Tạo cửa sổ con (Toplevel) cho chức năng tìm kiếm
    search_window = Toplevel(root)
    search_window.title('Tìm kiếm dữ liệu')  # Đặt tiêu đề cho cửa sổ
    search_window.geometry('300x250')  # Đặt kích thước cửa sổ

    # Label hiển thị hướng dẫn chọn cột
    Label(search_window, text='Chọn cột:', font=('Arial', 10)).pack(pady=10)

    # Combobox hiển thị danh sách các cột trong dữ liệu để người dùng chọn
    column_combobox = Combobox(
        search_window, values=["Tất cả các cột"] + list(Du_Lieu.columns), state='readonly'
    )
    column_combobox.current(0)  # Đặt giá trị mặc định là "Tất cả các cột"
    column_combobox.pack(pady=5)

    # Label hiển thị hướng dẫn nhập giá trị tìm kiếm
    Label(search_window, text='Nhập giá trị tìm kiếm:', font=('Arial', 10)).pack(pady=10)

    # Entry cho phép người dùng nhập giá trị cần tìm
    search_entry = Entry(search_window)
    search_entry.pack(pady=5)

    # Nút "Tìm kiếm" để thực hiện tìm kiếm khi được nhấn
    Button(search_window, text='Tìm kiếm', command=Apply_Search).pack(pady=20)
def Restore_Data():
    # Biến toàn cục để đảm bảo dữ liệu và sao lưu có thể truy cập được
    global Du_Lieu, Backup_Data

    # Nếu không có dữ liệu sao lưu, hiển thị thông báo lỗi
    if Backup_Data is None:
        messagebox.showerror('Lỗi', 'Không có dữ liệu nào để khôi phục!')
        return

    # Sao chép dữ liệu sao lưu để khôi phục về trạng thái ban đầu
    Du_Lieu = Backup_Data.copy()

    # Cập nhật Treeview (bảng hiển thị dữ liệu) để phản ánh dữ liệu đã khôi phục
    Update_Treeview()

    # Thông báo cho người dùng rằng dữ liệu đã được khôi phục
    messagebox.showinfo('Thông báo', 'Dữ liệu đã được khôi phục về trạng thái ban đầu!')



Button(crud_entry, text="Chọn file muốn đọc", bd=0,font="arial 12", bg="peachpuff", cursor="hand2", width=37, command=Open_Folder).place(x=20, y=0)
Button(crud_entry, text="Tạo dữ liệu mới cho file",font="arial 12", bd=0, bg="peachpuff", cursor="hand2", width=37, command=Create_Data).place(x=20, y=30)
Button(crud_entry, text="Chỉnh sửa dữ liệu",font="arial 12", bd=0, bg="peachpuff", cursor="hand2", width=37, command=Edit_Data).place(x=20, y=60)
Button(crud_entry, text="Khôi phục dữ liệu",font="arial 12", bd=0, bg="peachpuff", cursor="hand2", width=37,command=Restore_Data).place(x=20, y=90)
Button(crud_entry, text="Xóa dữ liệu",font="arial 12", bd=0, bg="peachpuff", cursor="hand2", width=37, command=Delete_Data).place(x=20, y=120)
Button(crud_entry, text="Tìm kiếm dữ liệu",font="arial 12", bd=0, bg="peachpuff", cursor="hand2", width=37, command=Search_Data).place(x=20, y=150)

Button(crud_entry, text="Tỉ lệ bệnh nhân theo loại đau ngực (cp)", font="arial 14", bd=0, bg=framebg, width=30, command=cp).place(x=20,y=200)
Button(crud_entry, text="Tỉ lệ bênh nhân theo giới tính", font="arial 14", bd=0, bg=framebg, width=30,command=sex).place(x=20, y=240)
Button(crud_entry, text="Lượng đường trong máu khi đói", font="arial 14", bd=0, bg=framebg, width=30,command=fbs).place(x=20, y=280)
Button(crud_entry, text="Điện tâm đồ khi nghỉ ngơi", font="arial 14", bd=0, bg=framebg, width=30,command=restecg).place(x=20, y=320)
Button(crud_entry, text="Đau ngực do gắng sức", font="arial 14", bd=0, bg=framebg, width=30,command=exng).place(x=20, y=360)
Button(crud_entry, text="Độ dốc trong bài kiểm tra gắng sức", font="arial 14", bd=0, bg=framebg, width=30,command=slp).place(x=20, y=400)
Button(crud_entry, text="Bất thường động mạch vành", font="arial 14", bd=0, bg=framebg, width=30,command=caa).place(x=20, y=440)
Button(crud_entry, text="Kết quả chụp quét Thallium", font="arial 14", bd=0, bg=framebg, width=30,command=thall).place(x=20, y=480)
Button(crud_entry, text="Phân phối tuổi", font="arial 14", bd=0, bg=framebg, width=30,command=age).place(x=20, y=520)
Button(crud_entry, text="Phân phối oldpeak", font="arial 14", bd=0, bg=framebg, width=30,command=trtbps).place(x=20, y=560)
Button(crud_entry, text="Phân phối cholesterol", font="arial 14", bd=0, bg=framebg, width=30,command=chol).place(x=20, y=600)
Button(crud_entry, text="Phân phối nhịp tim tối đa", font="arial 14", bd=0, bg=framebg, width=30,command=thalachh).place(x=20, y=640)
Button(crud_entry, text="Phân phối huyết áp", font="arial 14", bd=0, bg=framebg, width=30,command=oldpeak).place(x=20, y=680)
Button(crud_entry, text="Kết quả phân loại", font="arial 14", bd=0, bg=framebg, width=30,command=output).place(x=20, y=720)
root.mainloop()
