while True:
    try:
        age =  int(input('Enter your age: '))
    except ValueError:
        print("Enter your age corectlly.")
        continue
    if age <= 0:
       print("Age cant be lowe than 0 or be 0.")
       continue
    elif age < 13:
       print("You belong to group called children")
       break
    elif age <= 19:
       print("You belong to group called teenagers.")
       break
    elif  age <= 64:
       print("You are Adult.")
       break
    elif age > 65:
       print("You are senior.")
       break
