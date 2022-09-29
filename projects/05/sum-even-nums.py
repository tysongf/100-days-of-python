min = int(input("Minimum value > "))
max = int(input("Maximum value > "))

#Force minimum value to be even
if min % 2 > 0: min += 1

total_sum = 0
for n in range(min, max + 1, 2):
   total_sum += n

print(f"Total: {total_sum}")
