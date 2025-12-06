arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy","Ziomsonziomal"]
longest = arr[0]
i = 0
for i in arr:
    if len(i) > len(longest):
        longest = i


print('Names:',*arr)
print('Longest name:',longest)
