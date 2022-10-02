your_name = input("Enter your full name: ")
their_name = input("Enter their full name: ")

combined_str = (your_name + their_name).lower()

# TRUE LOVE

true_score = 0
true_score += combined_str.count('t')
true_score += combined_str.count('r')
true_score += combined_str.count('u')
true_score += combined_str.count('e')

love_score = 0
love_score += combined_str.count('l')
love_score += combined_str.count('o')
love_score += combined_str.count('v')
love_score += combined_str.count('e')

total_score = true_score * 10 + love_score

print(f"Your love score is: {total_score}")

if (total_score < 10) or (total_score > 90):
    print("You go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
    print("You are alright together")
