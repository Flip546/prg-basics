def f(palindrome):
    palindrome =str(palindrome)
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False
    

print (f())