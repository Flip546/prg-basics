# Calculates the sum of even numbers from 1 to a given number N

N = int(input('Enter number: '))
sum_even = 0

# 1. Inicjalizacja licznika (zastępuje start w range(1, ...))
i = 1 

# Calculate the sum of even numbers
# 2. Warunek kontynuacji (zastępuje koniec w range(..., N + 1))
while i <= N:
    if i % 2 == 0:
        sum_even += i
        
    # 3. Aktualizacja licznika (zastępuje automatyczne przejście w pętli for)
    i += 1 

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")