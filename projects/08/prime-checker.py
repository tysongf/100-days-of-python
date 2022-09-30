def checkPrime(num):
    divisors = 0
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

user_input = int(input("Enter a number: "))

if(checkPrime(user_input)): print(f"{user_input} is a prime number.")
else: print(f"{user_input} is not a prime number.")
