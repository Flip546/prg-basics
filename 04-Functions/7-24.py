def f(expression):
    if "+" in expression:
        a, b = expression.split("+")
        return int(a) + int(b)

    if "-" in expression:
        a, b = expression.split("-")
        return int(a) - int(b)

