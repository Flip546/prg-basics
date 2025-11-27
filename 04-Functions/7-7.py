def f(binary_number):
    binary_number = str(binary_number)
    return binary_number != "" and set(binary_number) <= {'0', '1'}



if __name__ == "__main__":
    print(f(1234567891200367))
 