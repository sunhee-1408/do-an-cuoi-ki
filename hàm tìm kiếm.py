
#LÀM ƠN THẰNG NÀO COP CÁI CODE NÀY ZÌA NHỚ XÓA MẤY CÁI NÚT CỦ ĐI RỒI CHẠY LÀM ƠN LÀM ƠN LÀM ƠN!!!!!!!!!!!


# Hàm tìm kiếm dữ liệu
def Search_Data():
    if Du_Lieu is None:
        messagebox.showerror('Lỗi', 'Vui lòng mở file trước khi tìm kiếm')
        return

    def Apply_Search():
        nonlocal search_window
        column=column_combobox.get()
        search_value=search_entry.get()

        if not search_value:
            messagebox.showerror('Lỗi', 'Vui lòng nhập giá trị cần tìm')
            return

        try:
            if column=="Tất cả các cột":
                # Tìm kiếm trên toàn bộ bảng
                filtered_data = Du_Lieu[
                    Du_Lieu.apply(lambda row: row.astype(str).str.contains(search_value, case=False, na=False).any(), axis=1)
                ]
            else:
                # Tìm kiếm trên một cột cụ thể
                filtered_data=Du_Lieu[Du_Lieu[column].astype(str).str.contains(search_value, case=False, na=False)]

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
    search_window=Toplevel(root)
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

# Thêm nút tìm kiếm dữ liệu vào giao diện
Button(crud_entry, text="Tìm kiếm dữ liệu", bd=1, bg=background, cursor="hand2", width=19, command=Search_Data).place(x=15, y=45)
Button(crud_entry, text="Chọn file để đọc", bd=1, bg=background, cursor="hand2", width=19, command=Open_Folder).place(x=15, y=10)
Button(crud_entry, text="Tạo dòng mới", bd=1, bg=background, cursor="hand2", width=19, command=Create_Data).place(x=15, y= 80)
Button(crud_entry, text="Khôi phục dữ liệu", bd=1, bg=background, cursor="hand2", width=19).place(x=15, y=115)
Button(crud_entry, text="Xóa dữ liệu", bd=1, bg=background, cursor="hand2", width=19).place(x=15, y=150)
Button(crud_entry, text='Chỉnh sửa dữ liệu', bd=1, bg=background, cursor='hand2', width=19).place(x=15, y=185)
