def f(number):
    for i in range (2, number):
         if number % i == 0:
              return False
    if number / 1 == number and number / number == 1:
        return True
    else:
        return False
    
if __name__ == "__main__":
        print(f(113))