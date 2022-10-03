hi_score = 0
scores = input("Enter a list of scores, separated by a space:\n").split()

for score in scores:
    score = int(score)
    if score > hi_score:
        hi_score = score

print(f"Highest Score: {hi_score}")
