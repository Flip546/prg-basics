# 1. Initialize the 2D array with zeros
# (Correcting the structure to be a list of lists)
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# 2. Use nested loops to modify the values
# 'i' represents the row index (0 to 4)
# 'j' represents the column index (0 to 4)
for i in range(5):
    for j in range(5):
        # We add 1 to the indices because the table starts at 1, not 0
        grid[i][j] = (i + 1) * (j + 1)

# 3. Print the array formatted as a table
for row in grid:
    for value in row:
        # Print value followed by a space, stay on the same line
        print(value, end=" ")
    # Move to the next line after finishing a row
    print()