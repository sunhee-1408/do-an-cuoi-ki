import pandas as pd
import matplotlib.pyplot as plt
file_path = 'heart.csv'
data = pd.read_csv(file_path)

bins = [25, 45, 60, 80]
age_count = pd.cut(data['age'], bins=bins).value_counts(sort=False)  # Nhóm tuổi và đếm số lượng
langs = [f"{int(bin.left)}-{int(bin.right)}" for bin in age_count.index]  # Tạo nhãn nhóm tuổi
values = age_count.values  # Lấy số lượng

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([-0.2, 0, 1, 1])

wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')
age_labels = {
    '25-45': '0 : bệnh nhân trưởng thành (25-45).',
    '45-60': '1 : bệnh nhân trung niên (45-60).',
    '60-80': '2 : bệnh nhân cao tuổi. (60-80)',
    
}
# Thêm chú thích
ax.legend(wedges, [age_labels[lang] for lang in langs], 

          title="Nhóm tuổi", 
          loc="center left", 
          bbox_to_anchor=(1.2, 0, 0.5, 1))
plt.show()
#______________________________________________________________________________________________



bins = [0, 90, 120, 200]
trtbps_count = pd.cut(data['trtbps'], bins=bins).value_counts(sort=False)  # Nhóm huyết áp và đếm số lượng
langs = [f"{int(bin.left)}-{int(bin.right)}" for bin in trtbps_count.index]  # Tạo nhãn nhóm huyết áp
values = trtbps_count.values  # Lấy số lượng

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([-0.2, 0, 1, 1])

wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')
trtbps_labels = {
    '0-90': '0 : bệnh nhân bị huyết áp thấp.',
    '90-120': '1 : bệnh nhân có huyết áp bình thường.',
    '120-200': '2 : bệnh nhân huyết áp cao.',
    
}
# Thêm chú thích
ax.legend(wedges, [trtbps_labels[lang] for lang in langs], 

          title="Huyết áp khi nghỉ ngơi (mmHg)", 
          loc="center left", 
          bbox_to_anchor=(1.2, 0, 0.5, 1))
plt.show()
#______________________________________________________________________________________________



bins = [0, 40, 200, 250]
chol_count = pd.cut(data['chol'], bins=bins).value_counts(sort=False)  # Nhóm Cholesterol và đếm số lượng
langs = [f"{int(bin.left)}-{int(bin.right)}" for bin in chol_count.index]  # Tạo nhãn nhóm Cholesterol
values = chol_count.values  # Lấy số lượng

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([-0.2, 0, 1, 1])

wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')
chol_labels = {
    '0-40': 'Cholesterol thấp.',
    '40-200': 'Cholesterol bình thường.',
    '200-250': 'Cholesterol cao',
    
}
# Thêm chú thích
ax.legend(wedges, [chol_labels[lang] for lang in langs], 

          title="Cholesterol(mg/dL)", 
          loc="center left", 
          bbox_to_anchor=(1.2, 0, 0.5, 1))
plt.show()



#______________________________________________________________________________________________
bins = [0, 60, 160, 250]
thalachh_count = pd.cut(data['thalachh'], bins=bins).value_counts(sort=False)  # Nhóm nhịp tim và đếm số lượng
langs = [f"{int(bin.left)}-{int(bin.right)}" for bin in thalachh_count.index]  # Tạo nhãn nhóm nịp tim
values = thalachh_count.values  # Lấy số lượng

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([-0.2, 0, 1, 1])

wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')
thalachh_labels = {
    '0-60': 'tần số nhịp tim thấp',
    '60-160': 'tần số nhịp tim bình thường',
    '160-250': 'tần số nhịp tim cao bất thường'
    
}
# Thêm chú thích
ax.legend(wedges, [thalachh_labels[lang] for lang in langs], 

          title="Chỉ số nhịp tim tối đa (BPM)", 
          loc="center left", 
          bbox_to_anchor=(1.2, 0, 0.5, 1))
plt.show()
#______________________________________________________________________________________________




bins = [0, 1, 2, 10]
oldpeak_count = pd.cut(data['oldpeak'], bins=bins).value_counts(sort=False)  # Nhóm nhịp tim và đếm số lượng
langs = [f"{bin.left:.1f}-{bin.right:.1f}" for bin in oldpeak_count.index]  # Tạo nhãn nhóm nịp tim
values = oldpeak_count.values  # Lấy số lượng

# Vẽ biểu đồ
fig = plt.figure()
ax = fig.add_axes([-0.2, 0, 1, 1])

wedges, texts, autotexts = ax.pie(values, labels=langs, autopct='%1.2f%%')
oldpeak_labels = {
    0: 'Tim bình thường, không có dấu hiệu thiếu máu cơ tim.',
    '0-1': 'Có thể bình thường hoặc mức độ thiếu máu cơ tim nhẹ.',
    '1-2': 'Thiếu máu cơ tim vừa, cần kiểm tra và chẩn đoán thêm.',
    '2-10': 'Thiếu máu cơ tim nghiêm trọng, nguy cơ cao, cần can thiệp y tế khẩn cấp.',
}
# Thêm chú thích
ax.legend(wedges, [oldpeak_labels[int(lang)] for lang in langs], 

          title="Mức độ Oldpeak", 
          loc="center left", 
          bbox_to_anchor=(1.2, 0, 0.5, 1))
plt.show()
#______________________________________________________________________________________________
