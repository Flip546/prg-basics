coin1 = 1
coin2 = 2
coin3 = 5

def  f(amount_to_pay):
    amount1 = (amount_to_pay // coin3)
    rest1 = (amount_to_pay % coin3)
    amount2 = (rest1 // coin2)
    rest2 = (amount2 %  coin2)
    amount3 = (rest2 // coin1)
    full = (amount1 + amount2 + amount3)
    return full

