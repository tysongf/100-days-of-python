# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols?\n"))
num_numbers = int(input(f"How many numbers?\n"))

characters = ""
for letter in range(1, num_letters + 1):
    characters += random.choice(letters)

for symbol in range(1, num_symbols + 1):
    characters += random.choice(symbols)

for number in range(1, num_numbers + 1):
    characters += random.choice(numbers)

password = "".join(random.sample(characters, len(characters)))

print(password)
