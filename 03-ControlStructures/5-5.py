###
# Sums numbers entered by user
#
total_sum = 0
arth = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1
    if count > 0:
        arth_average = total_sum/count
    else:
        arth_average = 0

    
print(f"Arthematic average is {arth_average}")
print(f"The total sum of the numbers is: {total_sum}")