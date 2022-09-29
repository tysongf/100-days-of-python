import random

sides = int(input("How many sides per dice? "))
dice = int(input("How many dice do you want to roll? "))

max = dice * sides
min = dice

roll = random.randint(min, max)

print(roll)
