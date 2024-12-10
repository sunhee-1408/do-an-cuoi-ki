import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Đọc dữ liệu
df = pd.read_csv("heart.csv", sep=',', header=0, index_col=0)

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

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([-0.2, 0, 1, 1])

wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')

thall_labels = {
    1: '3 : Norma',
    2: '6 :Fixed defect',
    3: '7 :Reversible defect'
}
# Thêm chú thích
ax.legend(wedges, [thall_labels[int(lang)] for lang in langs], 
          title="Độ dốc của đoạn ST cực đại trong bài kiểm tra gắng sức", 
          loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

plt.show()
#------------------------------------------------------
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
ax.legend(wedges, [thall_labels[int(lang)] for lang in langs], 
          title="Kết quả phân loại", 
          loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1))  # Vị trí chú thích

plt.show()