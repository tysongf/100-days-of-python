typical_lifespan = 87
weeks_per_year = 52
weeks_per_life = typical_lifespan * weeks_per_year

user_age = input("How old are you? ")
user_weeks = int(user_age) * 52
weeks_remaining = weeks_per_life - user_weeks

print(f"You have {weeks_remaining} weeks remaining. Use them wisely.")
