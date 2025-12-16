###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'
count = 0
with open('it_company.csv', 'r') as file:
   
   for line in file:
      if job_title in line :
          count +=1 
          print(f'{count}: {line}')
          
   
        
          
         

         
      