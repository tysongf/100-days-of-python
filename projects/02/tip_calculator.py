bill_total = float(input("Enter the bill total: "))
num_people = int(input("Number of people: "))
tip_percent = float(input("Tip %: "))

tip_total = round(bill_total * tip_percent / 100, 2)
grand_total = round(bill_total + tip_total, 2)
each_pay = round(grand_total / num_people, 2)

print(f"Subtotal: $ {bill_total:.2f}")
print(f"Tip:      $ {tip_total:.2f}")
print(f"Total:    $ {grand_total:.2f}\n")
print(f"Each person pays $ {each_pay:.2f}")
