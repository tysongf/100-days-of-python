
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    more = "y"
    result = False
    while more == "y":
        if(result):
            num1 = result
        else:
            num1 = float(input("First number: "))
        
        for op in operations:
            print(op)
        
        operation = input("Select an operation: ")
        
        num2 = float(input("Second number: "))

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")
        
        more = input("Perform another operation? (y)es / (n)o / (q)uit: ")
        if more == "n":
            calculator()
calculator()
