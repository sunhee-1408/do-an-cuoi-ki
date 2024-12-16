Backup_Data = None  # Lưu trữ bản sao để khôi phục dữ liệu
def Restore_Data():
    global Du_Lieu, Backup_Data

    if Backup_Data is None:
        messagebox.showerror('Lỗi', 'Không có dữ liệu nào để khôi phục!')
        return

    Du_Lieu = Backup_Data.copy()
    Update_Treeview()
    messagebox.showinfo('Thông báo', 'Dữ liệu đã được khôi phục về trạng thái ban đầu!')
