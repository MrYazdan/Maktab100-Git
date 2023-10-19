num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
operator = input("operator : ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)

print('hello mactab')
else:
    raise ValueError("Operation has invalid !")
    
