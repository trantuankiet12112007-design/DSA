def tim_ten(ds, ten_can_tim):
    ten_can_tim = ten_can_tim.lower()
    for i in range(len(ds)):
        if ds[i].lower() == ten_can_tim:
            return i
    return -1
ds = ["An", "Bình", "Châu"]
ten_can_tim = input("Nhập tên cần tìm: ")
print(tim_ten(ds,ten_can_tim))