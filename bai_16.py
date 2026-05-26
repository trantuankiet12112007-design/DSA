def phan_tu_gan_nhat(a, x):
    if not a:
        return None, -1
        
    vi_tri_gan_nhat = 0
    chenh_lech_min = abs(a[0] - x)
    
    for i in range(1, len(a)):
        chenh_lech_hien_tai = abs(a[i] - x)
        if chenh_lech_hien_tai < chenh_lech_min:
            chenh_lech_min = chenh_lech_hien_tai
            vi_tri_gan_nhat = i
            
    return a[vi_tri_gan_nhat], vi_tri_gan_nhat

a = [10, 22, 28, 29, 40]
gia_tri, vi_tri = phan_tu_gan_nhat(a, 26)
print(f"Phần tử gần 26 nhất là {gia_tri} tại vị trí {vi_tri}")