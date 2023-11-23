import string
import random

# Include letters, digits, and punctuation symbols from the string module
keyboard_symbols = string.ascii_letters + string.digits + string.punctuation

# Additional symbols commonly found on keyboards
additional_symbols = [
    '\n',  # newline
    '\t',  # tab
    '\r',  # carriage return
]

# Combine all symbols
all_symbols = keyboard_symbols + ''.join(additional_symbols)

# Convert the string of symbols to a list
symbols_array = list(all_symbols)

# Print the list of symbols
# print(symbols_array)

print("Welcome to the PyPassword Generator!")
nr_characters = int(
    input("How many characters would you like in your password?\n"))

password = []
for i in range(1, nr_characters + 1):
  password += random.choice(symbols_array)

final_password = ""
for i in password:
  final_password += i

print(f"Your password is: {final_password}")
