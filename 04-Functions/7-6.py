def hide(card_number):

    card_number = str(card_number)
    if len(card_number) != 16:
        return False
    
    return card_number[:2] + "*" * 10 + card_number[-4:]
    
    
    
    
if __name__ == "__main__":
    print(hide(1234567891200367))
 

