def tim_sinh_vien(danh_sach, ma_sv_tim):
    for sv in danh_sach:
        if sv['ma_sv'] == ma_sv_tim:
            print("Đã tìm thấy sinh viên:")
            print(f"- Mã SV: {sv['ma_sv']}")
            print(f"- Họ tên: {sv['ho_ten']}")
            print(f"- Điểm TB: {sv['diem_tb']}")
            return
    print("Thông báo: Không tìm thấy sinh viên có mã này.")

danh_sach_sv = [
    {'ma_sv': 'SV01', 'ho_ten': 'Nguyễn Văn A', 'diem_tb': 8.5},
    {'ma_sv': 'SV02', 'ho_ten': 'Trần Thị B', 'diem_tb': 7.2}
]
tim_sinh_vien(danh_sach_sv, 'SV02')