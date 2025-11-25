import keyboard

name = keyboard.input_string("Enter your name: ")
age = keyboard.input_integer("Enter your age: ")
price = keyboard.input_real("Enter price: ")
flag = keyboard.input_boolean("Do you agree?")

print(name, age, price, flag)
