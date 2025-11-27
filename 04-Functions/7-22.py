def f(name):
    result = ""

    for word in name.split():
        result += word[0]

    return result



print(f("Lord"))
# LotR
