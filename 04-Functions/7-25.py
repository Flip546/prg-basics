def f(x,y):
    total = 0
    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
         total += i

    return total


print(f(2,21))





