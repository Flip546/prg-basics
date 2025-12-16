with open('files.txt','r')as file:
    content = file.read()
    import re
    pattern = r'\w+\.\w{4}\b'
    match = re.findall(pattern,content)

    for i in match:
        print(i)
    