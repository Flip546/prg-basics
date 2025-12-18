def  f(number):
    stack = []
    orgnum = number
    if number == 0 :
        stack.append(0)

    while number > 0 :
        rest = number % 2
        stack.append(rest)
        number = number// 2
    binary = ""
    while len(stack) > 0:
        binary += str(stack.pop())


    return f"{orgnum} is in binary {binary}"

    




    
print(f(302))






