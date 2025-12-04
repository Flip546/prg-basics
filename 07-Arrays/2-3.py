# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
for rows in monthly_expenses:
    for cost in rows:
        food = monthly_expenses[0][0] + monthly_expenses[1][0] + monthly_expenses[2][0] + monthly_expenses[3][0]
        transport = monthly_expenses[0][1] + monthly_expenses[1][1] + monthly_expenses[2][1] + monthly_expenses[3][1]
        utilities = monthly_expenses[0][2] + monthly_expenses[1][2] + monthly_expenses[2][2] + monthly_expenses[3][2]
        week1 = monthly_expenses[0][0] + monthly_expenses[0][1] + monthly_expenses[0][2] 
        week2 = monthly_expenses[1][0] + monthly_expenses[1][1] + monthly_expenses[1][2] 
        week3 = monthly_expenses[2][0] + monthly_expenses[2][1] + monthly_expenses[2][2] 
        week4 = monthly_expenses[3][0] + monthly_expenses[3][1] + monthly_expenses[3][2] 
        total = week1 + week2 +week3 +week4

...
...

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:',total)