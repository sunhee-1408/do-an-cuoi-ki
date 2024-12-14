import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
data = pd.read_csv('heart.csv')

# 1. Phân phối tuổi (age)
plt.figure(figsize=(8, 6))
plt.hist(data['age'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("biểu đô phân phối độ tuổi của người bệnh")
plt.xlabel("Tuổi")
plt.ylabel("Số người")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 2. Phân phối huyết áp (trtbps)
plt.figure(figsize=(8, 6))
plt.hist(data['trtbps'], bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
plt.title("biểu đồ phân phối huyết áp bệnh nhân (mmHg)")
plt.xlabel("huyết áp nghỉ ngơi(mmHg)")
plt.ylabel("Count")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 3. Phân phối cholesterol (chol)
plt.figure(figsize=(8, 6))
plt.hist(data['chol'], bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title("Biểu đồ phân phối Cholesterol")
plt.xlabel("Cholesterol(mg/dL)")
plt.ylabel("số người")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 4. Phân phối nhịp tim tối đa (thalachh)
plt.figure(figsize=(8, 6))
plt.hist(data['thalachh'], bins=20, color='orange', edgecolor='black', alpha=0.7)
plt.title("Phân phối nhịp tim tối đa (thalachh)")
plt.xlabel("thalachh")
plt.ylabel("Count")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 5. Phân phối oldpeak
plt.figure(figsize=(8, 6))
plt.hist(data['oldpeak'], bins=20, color='purple', edgecolor='black', alpha=0.7)
plt.title("Phân phối oldpeak")
plt.xlabel("oldpeak")
plt.ylabel("Count")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
