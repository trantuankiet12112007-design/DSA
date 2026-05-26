def them_lien_he(danh_ba, ten, sdt):
    danh_ba.append({'ten': ten, 'sdt': sdt})
    print("Đã thêm liên hệ thành công!")

def tim_sdt_theo_ten(danh_ba, ten_tim):
    for lh in danh_ba:
        if lh['ten'].lower() == ten_tim.lower():
            return lh['sdt']
    return None

def tim_ten_theo_sdt(danh_ba, sdt_tim):
    for lh in danh_ba:
        if lh['sdt'] == sdt_tim:
            return lh['ten']
    return None

def dem_theo_dau_so(danh_ba, dau_so):
    dem = 0
    for lh in danh_ba:
        if lh['sdt'].startswith(dau_so):
            dem += 1
    return dem

def chuong_trinh_danh_ba():
    danh_ba = []
    while True:
        print("\n--- QUẢN LÝ DANH BẠ ---")
        print("1. Thêm liên hệ")
        print("2. Tìm số điện thoại theo tên")
        print("3. Tìm tên theo số điện thoại")
        print("4. Đếm số liên hệ theo đầu số")
        print("5. Thoát")
        
        chon = input("Chọn chức năng (1-5): ")
        
        if chon == '1':
            ten = input("Nhập tên: ")
            sdt = input("Nhập số điện thoại: ")
            them_lien_he(danh_ba, ten, sdt)
        elif chon == '2':
            ten = input("Nhập tên cần tìm: ")
            kq = tim_sdt_theo_ten(danh_ba, ten)
            if kq:
                print(f"Số điện thoại của {ten} là: {kq}")
            else:
                print("Không tìm thấy tên trong danh bạ.")
        elif chon == '3':
            sdt = input("Nhập số điện thoại cần tìm: ")
            kq = tim_ten_theo_sdt(danh_ba, sdt)
            if kq:
                print(f"Số điện thoại {sdt} thuộc về: {kq}")
            else:
                print("Không tìm thấy số điện thoại trong danh bạ.")
        elif chon == '4':
            dau_so = input("Nhập đầu số (ví dụ 090): ")
            kq = dem_theo_dau_so(danh_ba, dau_so)
            print(f"Có {kq} liên hệ bắt đầu bằng đầu số {dau_so}.")
        elif chon == '5':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
chuong_trinh_danh_ba()
