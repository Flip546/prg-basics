try:
  text1 = input('Enter file name: ')
  print(f'File name: {text1}')
  with open(text1, 'r')as file:
   content = file.read()
   count = 0
   for i in content:
      count += 1
   lines_list = content.splitlines()
   lines = len(lines_list)
   word_list = content.split()
   words = len(word_list)


   print(f'Number of characters: {count}')
   print(f'Number of lines: {lines}')
   print(f'Number of words: {words}')
except FileNotFoundError:
   print('Nie ma takiego pliku')
