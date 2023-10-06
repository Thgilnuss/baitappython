#Câu 1
print('''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are''')
#Câu 3
import datetime
hien_tai = datetime.datetime.now()
ngay = hien_tai.strftime("%d/%m/%Y")
gio = hien_tai.strftime("%H:%M:%S")
print(f"Ngày hiện tại: {ngay}")
print(f"Giờ hiện tại: {gio}")

#Câu 4
def kiem_tra_ban_kinh():
    while True:
        r = float(input("Nhập vào bán kính của đường tròn r = "))
        if r>0:
            return r
        else:
            print("Bán kính không hợp lệ")
def tinh_dien_tich(r):
    S = 3.14*r**2
    return S
r = kiem_tra_ban_kinh()
dien_tich = tinh_dien_tich(r)
print(f"Diện tích của đường tròn có bán kính r = {r} là: 3.14*{r}^2 = {dien_tich}")
#Câu 7
def lay_phan_mo_rong(f):
    phan_mo_rong = filename.split(".")[-1]
    return phan_mo_rong
filename = str(input("Nhập vào tên tệp: "))
phan_mo_rong = lay_phan_mo_rong(filename)
print(f"Phần mở rộng của file: {filename} là {phan_mo_rong}")

#Câu 10
n = int(input("Nhập vào số nguyên n = "))
nn = n*10+n
nnn = n*100+nn
kq = n+nn+nnn
print(f"Giá trị của {n}+{nn}+{nnn} = {kq}")
#Câu 28
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
for x in numbers:
    if x == 237:
        print(x)
        break
    elif x % 2 == 0:
        print(x)
#Câu 29
def mang_khong_trung(mang1, mang2):
    mang_ket_qua = []
    for so in mang1:
        if so not in mang2:
            mang_ket_qua.append(so)
    return mang_ket_qua
mang1 = [1, 2, 3, 4, 5, 6]
mang2 = [3, 5, 7, 9]

mang_ket_qua = mang_khong_trung(mang1, mang2)
print(f"Mảng các số không trùng: {mang_ket_qua}")
#Câu 30
def tinh_dien_tich_tam_giac():
    while True:
        b = float(input("Nhập vào chiều dài đáy của tam giác b = "))
        h = float(input("Nhập vào chiều cao của tam giác h = "))
        if b > 0 and h > 0:
            return 1/2*b*h
        else:
            print("Thông số nhập vào không hợp lệ!")
S = tinh_dien_tich_tam_giac()
print(f"Diện tích của tam giác bằng {S}")

    


