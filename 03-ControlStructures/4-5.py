###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    char_code = ord(char)
    # add one to the character's ode
    newc_code = char_code + 1
    # replace new character code with its
    encrypted_char = chr(new_code)
    # corresponding character (use chr())
    encrypted_text += encrypted_char
    # add encrypted character to encrypted text
    ...
print(f"plain text: {plain_text}")
print(f"encrypted_text: {encrypted_text}")