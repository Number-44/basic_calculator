import operator

# Define supported operations
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

# Input handling with validation
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter integers only.")
    exit()

# Get operator
op = input("Enter the operator (+, -, *, /): ")
if op not in operations:
    print("Invalid operator! Please choose from +, -, *, /.")
    exit()

# Perform the operation
if op == "/" and num2 == 0:
    print("Division by zero is undefined!")
else:
    result = operations[op](num1, num2)
    print(f"The result of {num1} {op} {num2} is :   \"   {result}   \"")
