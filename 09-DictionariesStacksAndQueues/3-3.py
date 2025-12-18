def brackets_ok(expression):
    # Tworzymy stos jako zwykłą listę
    stack = []
    
    # Słownik par nawiasów
    matching_brackets = {')': '(', '}': '{', ']': '['}
    opening = "({["
    closing = ")}]"

    for char in expression:
        # 1. Jeśli to nawias otwierający, dodajemy go na koniec listy (wierzch stosu)
        if char in opening:
            stack.append(char)
        
        # 2. Jeśli to nawias zamykający
        elif char in closing:
            # Jeśli lista jest pusta, a mamy nawias zamykający -> błąd!
            if not stack:
                return False
            
            # Zdejmujemy ostatni element z listy metodą pop()
            last_open = stack.pop()
            if last_open != matching_brackets[char]:
                return False
                
    # 3. Na koniec sprawdzamy, czy lista jest pusta (czy wszystkie pary zamknięte)
    return len(stack) == 0

# Testowanie wyrażeń
expressions = [
    "[(2+3)*4+5]/6-{(7*8)+[4]}", # brackets ok
    "[(2+3]/4)",                 # brackets not correct
    "(2-3*4+(5/6)"               # brackets not correct
]

for i, expr in enumerate(expressions, 1):
    if brackets_ok(expr):
        print(f"Expression{i}: Brackets are OK")
    else:
        print(f"Expression{i}: Brackets are NOT correct")