def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content



file_content = read_from_file('pets.txt')
file_items = file_content.split('#')
count = 0
for i in file_content:
   count += 1

print(f"{file_content} COUNT: {count}")
   

