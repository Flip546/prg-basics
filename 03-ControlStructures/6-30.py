nums = list(range(1, 50))


for c in range(7):
    row = nums[c : 49 : 7]
    print(*row)