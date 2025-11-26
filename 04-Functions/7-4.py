def letter1(text,letter):
    return text.count(letter)


    

def main():
    letter = input('What letter to check how many times it appears: ')
    text = input('Emter text to check: ')
    print(letter1(text, letter))
if __name__ == "__main__":
 main()