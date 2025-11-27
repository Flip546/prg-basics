def f(number, even):
    number = str(number)
    total = 0

    for digit in number:
        d = int(digit)

        if even and d % 2 == 0:
            total += d
        if not even and d % 2 != 0:
            total += d

    return total
print(f(123456, True))    # 2+4+6 = 12
print(f(123456, False))   # 1+3+5 = 9
