import random

sides = int(input("How many sides per dice? "))
dice = int(input("How many dice do you want to roll? "))

max_val = dice * sides
min_val = dice

roll = random.randint(min_val, max_val)

print(roll)
