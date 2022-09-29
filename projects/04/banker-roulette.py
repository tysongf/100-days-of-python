import random
input_str = input("Enter everyone's name, separated by commas: ")
bankers = input_str.split(", ")
print(bankers)

roll = random.randint(0, len(bankers) - 1)

print(f"{bankers[roll]} pays the bill!")

random_choice = random.choice(bankers)

print(f"{random_choice} gets to ride shotgun!")
