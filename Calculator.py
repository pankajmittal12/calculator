def add(num, num2):
    return num + num2

def subtract(num, num2):
    return num - num2

def multiply(num, num2):
    return num * num2

def divide(num, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num / num2

def power(num, num2):
    return num ** num2

def square_root(num):
    if num < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return num ** 0.5

def modulus(num, num2):
    if num2 == 0:
        raise ValueError("Cannot perform modulus with zero.")
    return num % num2

enter = input("Enter the operation (add, subtract, multiply, divide, power, square_root, modulus): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if enter == "add":
    print("Result:", add(num1, num2))   
elif enter == "subtract":
    print("Result:", subtract(num1, num2))
elif enter == "multiply":
    print("Result:", multiply(num1, num2))
elif enter == "divide":
    try:
        print("Result:", divide(num1, num2))
    except ValueError as e:
        print(e)
elif enter == "power":
    print("Result:", power(num1, num2))
elif enter == "square_root":
    try:
        print("Result:", square_root(num1))
    except ValueError as e:
        print(e)
elif enter == "modulus":
    try:
        print("Result:", modulus(num1, num2))
    except ValueError as e:
        print(e)