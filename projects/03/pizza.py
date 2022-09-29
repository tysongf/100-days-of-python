print("Welcome to Python Pizza!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

subtotal = 0

if size == "S" or size == "s":
   subtotal = 15
   pep_price = 2
elif size == "M" or size == "m":
   subtotal = 20
   pep_price = 3
elif size == "L" or size == "l":
   subtotal = 25
   pep_price = 3

if add_pepperoni == "Y" or add_pepperoni == "y":
   subtotal += pep_price

if extra_cheese == "Y" or extra_cheese == "y":
   subtotal += 1

print(f"Your final bill is: ${subtotal:.2f}")


