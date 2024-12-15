Backup_Data = None  # Lưu trữ bản sao để khôi phục dữ liệu
def Restore_Data():
    global Du_Lieu, Backup_Data

    if Backup_Data is None:
        messagebox.showerror('Lỗi', 'Không có dữ liệu nào để khôi phục!')
        return

    Du_Lieu = Backup_Data.copy()
    Update_Treeview()
    messagebox.showinfo('Thông báo', 'Dữ liệu đã được khôi phục về trạng thái ban đầu!')
Button(crud_entry, text="Khôi phục dữ liệu", bd=1, bg=background, cursor="hand2", width=19, command=Restore_Data).place(x=15, y=100)