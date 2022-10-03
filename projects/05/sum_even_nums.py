min_val = int(input("Minimum value > "))
max_val = int(input("Maximum value > "))

# Force minimum value to be even
if min_val % 2 > 0: min_val += 1

total_sum = 0
for n in range(min_val, max_val + 1, 2):
    total_sum += n

print(f"Total: {total_sum}")
