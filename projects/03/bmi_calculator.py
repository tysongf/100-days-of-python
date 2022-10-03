height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height ** 2), 2)

if bmi < 18.5:
    status = "underweight"
elif bmi < 25:
    status = "normal"
elif bmi < 30:
    status = "overweight"
elif bmi < 35:
    status = "obese"
else:
    status = "clinically obese"

print(f"Your BMI is {bmi}")
print(f"Your weight is: {status}")
