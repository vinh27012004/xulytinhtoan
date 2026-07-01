# demo.py — chạy thử các phép tính cộng, trừ, nhân
# Cách chạy:  python demo.py
#   hoặc:      python demo.py 8 3        (dùng 2 số của bạn)

import sys

from calculator import cong, tru, nhan, chia, luy_thua

# Đảm bảo in được tiếng Việt trên terminal Windows (cp1252)
sys.stdout.reconfigure(encoding="utf-8")


def main():
    args = sys.argv[1:]
    try:
        a = float(args[0]) if len(args) > 0 else 12
        b = float(args[1]) if len(args) > 1 else 4
    except ValueError:
        print("Vui lòng nhập 2 số hợp lệ. Ví dụ: python demo.py 8 3")
        sys.exit(1)

    # Bỏ phần .0 nếu là số nguyên cho gọn
    def fmt(x):
        return int(x) if x == int(x) else x

    a, b = fmt(a), fmt(b)

    print(f"Hai số: a = {a}, b = {b}\n")
    print(f"Cộng:     {a} + {b} = {fmt(cong(a, b))}")
    print(f"Trừ:      {a} - {b} = {fmt(tru(a, b))}")
    print(f"Nhân:     {a} × {b} = {fmt(nhan(a, b))}")

    if b == 0:
        print(f"Chia:     {a} ÷ {b} = không thể chia cho 0")
    else:
        print(f"Chia:     {a} ÷ {b} = {fmt(chia(a, b))}")

    print(f"Lũy thừa: {a} ^ {b} = {fmt(luy_thua(a, b))}")


if __name__ == "__main__":
    main()
