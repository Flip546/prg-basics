sentence = 'I completely agree with you'
sent_split = sentence.split()
result = list(map(lambda x:len(x) , sent_split))
print(result)