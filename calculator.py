# calculator.py — các hàm xử lý phép tính cơ bản


def cong(a, b):
    return a + b


def tru(a, b):
    return a - b


def nhan(a, b):
    return a * b


def tinh(a, b, pheptoan):
    """Tính theo phép toán truyền vào: '+', '-', '*'."""
    if pheptoan == '+':
        return cong(a, b)
    if pheptoan == '-':
        return tru(a, b)
    if pheptoan == '*':
        return nhan(a, b)
    raise ValueError(f"Phép toán không hỗ trợ: {pheptoan}")
