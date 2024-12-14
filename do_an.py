import pandas as pd # được sử dụng để xử lý và phân tích dữ liệu
import numpy as np # hữu ích cho các phép tính số học và xử lý mảng.
import matplotlib # dùng để tạo các biểu đồ và hình ảnh minh họa
import matplotlib.pyplot as plt #tạo các biểu đồ và hình ảnh trực quan.
import seaborn as sns #giúp tạo các biểu đồ thống kê đẹp mắt và dễ sử dụng.
import warnings
warnings.filterwarnings('ignore') #Bỏ qua các cảnh báo để đầu ra gọn gàng hơn



# Đọc dữ liệu
df = pd.read_csv("heart.csv", sep=',')

#----------------------------------------------------------------------------------------------------
# Xử lý dữ liệu
cp_count = df['cp'].value_counts()  # Đếm số lượng từng loại đau ngực
langs = cp_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
values = cp_count.values  # Lấy số lượng

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

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
#--------------------------------------------------------------------------------------------------
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
          title="giới tính", 
          loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

plt.show()

#--------------------------------------------------------------------------
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
#-----------------------------------------------------------------------
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

#-----------------------------------------------------------------------
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
#-----------------------------------------------------------------
            #Đoạn ST là một phần quan trọng trong biểu đồ ECG và sự thay đổi của nó (dạng dốc lên hoặc dốc xuống) có thể cung cấp thông tin về tình trạng tim.
            #Độ dốc âm tính (0) có thể chỉ ra thiếu máu cơ tim, một dấu hiệu cho thấy máu không thể lưu thông đúng cách qua động mạch vành trong khi gắng sức.
            #Độ dốc dương tính (2) có thể là dấu hiệu tốt, cho thấy tim phản ứng bình thường với gắng sức.
            #Độ dốc phẳng (1) có thể cần phải theo dõi thêm để xác định xem có bất kỳ vấn đề tiềm ẩn nào không.
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
#-------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------
thall_count = df['thall'].value_counts()  # Đếm số lượng từng loại đau ngực
langs = thall_count.index.astype(str)  # Chuyển chỉ mục thành chuỗi
values = thall_count.values  # Lấy số lượng

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
#---------------------------------------------------------------------
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

#------------------------------------------------------------------
sns.set(style="whitegrid")

# 1. Phân phối tuổi (age)
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], bins=20, color='skyblue', alpha=0.7,kde=True)
plt.title("biểu đô phân phối độ tuổi của người bệnh")
plt.xlabel("Tuổi")
plt.ylabel("Số người")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 2. Phân phối huyết áp (trtbps)
plt.figure(figsize=(8, 6))
sns.histplot(df['trtbps'], bins=20, color='lightcoral', alpha=0.7,kde=True)
plt.title("biểu đồ phân phối huyết áp bệnh nhân (mmHg)")
plt.xlabel("huyết áp nghỉ ngơi(mmHg)")
plt.ylabel("Count")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 3. Phân phối cholesterol (chol)
plt.figure(figsize=(8, 6))
sns.histplot(df['chol'], bins=20, color='lightgreen', alpha=0.7,kde=True)
plt.title("Biểu đồ phân phối Cholesterol")
plt.xlabel("Cholesterol(mg/dL)")
plt.ylabel("số người")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 4. Phân phối nhịp tim tối đa (thalachh)
plt.figure(figsize=(8, 6))
sns.histplot(df['thalachh'], bins=20, color='orange', alpha=0.7,kde=True)
plt.title("Phân phối nhịp tim tối đa (thalachh)")
plt.xlabel("thalachh")
plt.ylabel("Count")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 5. Phân phối oldpeak
plt.figure(figsize=(8, 6))
sns.histplot(df['oldpeak'], bins=20, color='purple', alpha=0.7,kde=True)
plt.title("Phân phối oldpeak")
plt.xlabel("oldpeak")
plt.ylabel("Count")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
