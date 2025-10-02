def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if y == 0:
        return "Error! Division by zero."
    return a / b

print("Welcome to Most Basic Calculator")

operation = input("What would you like to do? \n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n ")

if operation == "1":
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = add(number1, number2)
elif operation == "2":
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = sub(number1, number2)
elif operation == "3":
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = mul(number1, number2)
elif operation == "4":
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = div(number1, number2)
print("The result is:", result)