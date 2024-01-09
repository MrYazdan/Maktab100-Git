try:
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    # Here you could add more logic, such as requesting input again or exiting the program.

operator = input("Operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "//":
    print(num1 // num2)
elif operator == "/":
    try:
        if num2 == 0:
            raise ZeroDivisionError
        print("Div:", num1 / num2)
        print("-" * 100)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
elif operator == "*":
    print(num1 * num2)
elif operator == "**":
    print(num1 ** num2)
else:
    print("Error: Invalid operation!")
