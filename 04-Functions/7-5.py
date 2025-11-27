def cos(range1,range2,number):
    if range1<number<range2:
        return 'IN range'
    else:
        return 'Not in range'
def main():
    range1 = int(input('Enter the starting point of range: '))
    range2 = int(input('Enter the ending point of range: '))
    number = int(input('Enter the number to check if it is in range: '))
    print(cos(range1,range2,number))
 
if __name__ == "__main__":
 main()


    
    