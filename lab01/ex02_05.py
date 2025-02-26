so_gio_lam = float(input("Nhập số giờ làm của nhân viên: "))
luong_gio_tieu_chuan = float(input("Nhập lương theo giờ làm tiêu chuẩn: "))
gio_tieu_chuan_moi_tuan = 44

gio_tieu_chuan = so_gio_lam if so_gio_lam < gio_tieu_chuan_moi_tuan else gio_tieu_chuan_moi_tuan
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan_moi_tuan)

tien_thuc_nhan = gio_tieu_chuan * luong_gio_tieu_chuan + gio_vuot_chuan*luong_gio_tieu_chuan*1.5

print("Số tiền mà nhân viên nhận được là: ", tien_thuc_nhan)