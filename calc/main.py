num1 = float(input("Number 1 : "))
num2 = float(input("Number 2 : "))
operator = input("operator : ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "//":
    print(num1//num2)
elif operator == "/":
    if num2==0:
        raise ZeroDivisionError
    print("Div:", num1/num2)
    print("-" * 100)
elif operator == "*":
    print(num1*num2)
elif operator == "**":
    print(num1**num2)
else:
    raise ValueError("Operation has invalid !")
