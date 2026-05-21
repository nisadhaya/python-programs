num1 = float(input("First number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Second number: "))

if op == '+': print("Result:", num1 + num2)
elif op == '-': print("Result:", num1 - num2)
elif op == '*': print("Result:", num1 * num2)
elif op == '/': print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
else: print("Invalid operator")
