text = input('Enter text to check: ')
import re
pattern = r'[aeiouy]'
Result = re.findall(pattern,text,re.IGNORECASE)
print (Result)
