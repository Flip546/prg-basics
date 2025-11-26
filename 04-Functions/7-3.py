#### Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year. In a separate module, define a function month(n) that returns a month name based on the month number (values from 1 to 12). Then, write a program to print the name of the month 7. Import the module with the created function. Sample result:

###Enter month number: 9
#The name of month 9 is September

def month(n):

    months = [
 'January',
 'February',
 'March',
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December'
    ]
    if  n <=12 and n != 0:
        return months[n - 1]

    raise ValueError('INCORRECT NUMBER OF MONTH')

    
def main():
    try: 
     n = int(input('Enter number of the month: '))
     print(month(n))
    except ValueError as e:
       print(e)


    

if __name__ == "__main__":
 main()

