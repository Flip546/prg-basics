from my_arrays import (
    second_largest,smallest_largest
    ,diffrence,med,string
)
numbers = [7, 3, 8, 5, 2]
print(f"Numbers: {', '.join(map(str, numbers))}\n")
mediana = med(numbers)
sec_larg = second_largest(numbers)
maksmin = smallest_largest(numbers)
dif = diffrence(numbers)
stra = string(numbers)


print(f'Mediana: {mediana}')
print(f'Second largest: {sec_larg}')
print(f'Maks and min number: {maksmin}')
print(f'Diffrence: {dif}')
print(f"String: {stra}")
