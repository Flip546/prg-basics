# Simple beginner-friendly dog age converter
# First 2 dog years = 10.5 human years each
# Every year after = 4 human years

age_str = int(input("Enter your dog's age in human years: "))
dogyears = 0
if age_str <= 2:
    dogyears = age_str * 10.5
else:
    dogyears = 21 + (age_str -2) * 4

print(f"The dog's age in dog's years is {int(dogyears)} years.")