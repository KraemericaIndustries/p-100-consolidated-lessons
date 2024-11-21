import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
addition = add

def subtract(n1, n2):
    return n1 - n2
subtraction = subtract

def multiply(n1, n2):
    return n1 * n2
multiplication = multiply

def divide(n1, n2):
    return n1 / n2
division = divide

operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division}

first_number = float(input("What's the first number: "))

resume = "y"

while resume =="y":
    operator = (input("+\n-\n*\n/\nPick an operation: "))
    second_number = float(input("What's the next number: "))

    result = operations[operator](first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")

    resume = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    first_number = result