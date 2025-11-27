def f(number):
    number = str(number)
    total = 0
    for i in number:
        if number.count(i) > 1:
            total += int(i)
    return total
    
    
print(f(1027))       # 0
print(f(230335))     # 9
print(f(513553007))  # 21
