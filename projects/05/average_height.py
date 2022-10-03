# Average Height = Total Height / Number of Students

total_height = 0
num_students = 0

heights = input("Enter a list of student heights, separated by a space:\n").split()

for n in range(0, len(heights)):
    heights[n] = int(heights[n])

for h in heights:
    total_height += h
    num_students += 1

print(f"Total Height: {total_height}")
print(f"Average Height: {total_height / num_students}")
