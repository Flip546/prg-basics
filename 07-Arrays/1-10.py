###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer == True:
      correct_answers += 1

# calculates the number of incorrect answers
incorrect_answer = 0
for x in test_results:
   if x == False:
      incorrect_answer += 1
   

# calculates the percentage of correct answers
percet = correct_answers/len(test_results) *100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', len(test_results))
print('Number of correct answers:', (correct_answers) )
print('Number of incorrect', (incorrect_answer))
print('Percentage',(percet))