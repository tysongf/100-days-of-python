typical_lifespan = 87

user_age = int(input("How old are you? "))
user_years_remaining = typical_lifespan - user_age
months_remaining = user_years_remaining * 12
weeks_remaining = user_years_remaining * 52
days_remaining = user_years_remaining * 365

print(f"You have {months_remaining} months remaining.")
print(f"You have {weeks_remaining} weeks remaining.")
print(f"You have {days_remaining} days remaining.")
