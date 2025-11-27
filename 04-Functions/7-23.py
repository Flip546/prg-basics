def f(password):
    password = str(password)
    if len(password)>6 and len(password) == len(set(password)):
     return True
    else:
       return False
    



print(f(''))