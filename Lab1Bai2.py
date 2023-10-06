#Bài 1
def Tong(a, b):
    return a+b
def Chia(a, b):
    return a/b
def Luy_thua(a, b):
    return a**b
a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
print(f"{a} + {b} = {Tong(a, b)}")
print(f"{a} / {b} = {Chia(a, b)}")
print(f"{a} lũy thừa {b} = {Luy_thua(a, b)}")

#Bài 2
def dien_tich_hinh_cn(a, b):
    return a*b
a = float(input("Nhập vào chiều dài của hình chữ nhật: "))
b = float(input("Nhập vào chiều rộng của hình chữ nhật: "))
print(f"Diện tích của hình chữ nhật có chiều dài là {a} và chiều rộng là {b} bằng {dien_tich_hinh_cn(a, b)}")

#Bài 3
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def xuat_so_nguyen_to_trong_khoang(start, end):
    for num in range(start, end + 1):
        if la_so_nguyen_to(num):
            print(num, end=" ")

start = int(input("Nhập đầu khoảng: "))
end = int(input("Nhập cuối khoảng: "))

print(f"Các số nguyên tố từ {start} đến {end} là:")
xuat_so_nguyen_to_trong_khoang(start, end)
print(" ")

#Bài 4
def la_so_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b

    return False

a = int(input("Nhập một số nguyên: "))

if la_so_fibonacci(a):
    print(f"{a} là số Fibonacci")
else:
    print(f"{a} không là số Fibonacci")

#Bài 5.1 Sử dụng đệ quy
def tim_so_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)
n = int(input("Nhập số thứ tự của số Fibonacci (n >= 0): "))
if n < 0:
    print("Vui lòng nhập số không âm.")
else:
    result = tim_so_fibonacci(n)
    print(f"Số Fibonacci thứ {n} là: {result}")

#Bài 5.2 Không sử dụng đệ quy
def tim_so_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_prev = 0
    fib_current = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_current
        fib_prev, fib_current = fib_current, fib_next

    return fib_current

n = int(input("Nhập số thứ tự của số Fibonacci (n >= 0): "))
if n < 0:
    print("Vui lòng nhập số không âm.")
else:
    result = tim_so_fibonacci(n)
    print(f"Số Fibonacci thứ {n} là: {result}")

#Bài 6.1 Sử dụng đệ quy
def tong_n_so_fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci(n) + tong_n_so_fibonacci_de_quy(n - 1)

n = int(input("Nhập số n: "))
if n < 0:
    print("Vui lòng nhập số không âm.")
else:
    result = tong_n_so_fibonacci_de_quy(n)
    print(f"Tổng {n} số Fibonacci đầu tiên là: {result}")

#Bài 6.2 Không sử dụng đệ quy
def tong_n_so_fibonacci_khong_de_quy(n):
    if n <= 0:
        return 0

    fib_sum = 0
    fib_prev = 0
    fib_current = 1

    for _ in range(n):
        fib_sum += fib_prev
        fib_prev, fib_current = fib_current, fib_prev + fib_current

    return fib_sum

n = int(input("Nhập số n: "))
if n < 0:
    print("Vui lòng nhập số không âm.")
else:
    result = tong_n_so_fibonacci_khong_de_quy(n)
    print(f"Tổng {n} số Fibonacci đầu tiên là: {result}")

#Bài 7
def tinh_tong_can_bac_hai(n):
    if n <= 0:
        return 0
    
    total = 0
    for i in range(1, n + 1):
        total += i ** 0.5
    
    return total

n = int(input("Nhập số n: "))
if n < 0:
    print("Vui lòng nhập số không âm.")
else:
    result = tinh_tong_can_bac_hai(n)
    print(f"Tổng căn bậc hai của {n} số nguyên đầu tiên là: {result:.2f}")

#Bài 8
import math

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        return "Phương trình vô nghiệm"

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là phương trình bậc hai.")
else:
    ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
    print("Kết quả:")
    print(ket_qua)

#Bài 9
def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)

n = int(input("Nhập một số nguyên dương: "))
if n < 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    result = tinh_giai_thua(n)
    print(f"{n}! = {result}")

#Bài 10

#Bài 11
def chuyen_doi_thoi_gian(so_giay):
    gio = so_giay // 3600
    so_giay %= 3600
    phut = so_giay // 60
    giay = so_giay % 60
    return gio, phut, giay

so_giay = int(input("Nhập số giây: "))
if so_giay < 0:
    print("Vui lòng nhập số không âm.")
else:
    gio, phut, giay = chuyen_doi_thoi_gian(so_giay)
    print(f"Kết quả: {gio}:{phut}:{giay}")

#Bài 12
#.1
def xuat_so_le_khong_chia_het_cho_5(arr):
    for num in arr:
        if num % 2 != 0 and num % 5 != 0:
            print(num, end=" ")
#.2
def xuat_cac_so_fibonacci(arr):
    for num in arr:
        if la_so_fibonacci(num):
            print(num, end=" ")
#.3
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def tim_so_nguyen_to_lon_nhat(arr):
    max_prime = None
    for num in arr:
        if la_so_nguyen_to(num):
            if max_prime is None or num > max_prime:
                max_prime = num
    return max_prime
arr = []
n = int(input("Nhập số phần tử trong mảng: "))
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(num)

print("Các số lẻ không chia hết cho 5 trong mảng:")
xuat_so_le_khong_chia_het_cho_5(arr)

print("Các số Fibonacci trong mảng:")
xuat_cac_so_fibonacci(arr)

so_nguyen_to_lon_nhat = tim_so_nguyen_to_lon_nhat(arr)
if so_nguyen_to_lon_nhat is None:
    print("Không có số nguyên tố trong mảng.")
else:
    print(f"Số nguyên tố lớn nhất trong mảng là: {so_nguyen_to_lon_nhat}")