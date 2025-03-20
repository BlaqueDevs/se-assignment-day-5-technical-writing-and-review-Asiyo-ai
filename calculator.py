# Ask the user for two numbers and a mathematical operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check if division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Invalid operation.")

# If a valid operation was entered, print the result
if operation in ["+", "-", "*", "/"]:
    print(f"The result of {num1} {operation} {num2} is: {result}")
