import math
def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "undefined"
    return x/y
def power(x, y):
    return x ** y
def squareroot(x):
    if x < 0:
        return "i * " + str(math.sqrt(abs(x)))
    return math.sqrt(x)
def modulo(x, y):
    return x % y
def trigonometry():
    print('''Select Operation(2): 
    1. Arc Sin
    2. Arc Cos
    3. Arc Tan''')
    choice2 = input("Enter choice from 1-3: ")
    if choice2 in ('1', '2', '3'):
        tri = float(input("Enter the degrees: "))
        if choice2 == '1':
            print(f"arc sin({tri}) = {math.sin(tri)}")
        elif choice2 == '2':
            print(f"arc cos({tri}) = {math.cos(tri)}")
        elif choice2 == '3':
            print(f"arc tan({tri}) = {math.tan(tri)}")
    else:
        print("Input invalid")
def factorial(x):
    if x < 0:
        return "no factorials for negatives"
    if x == 0 or x == 1:
        return x
    return x * factorial(x-1)
    
while True:
    print('''Select Operation:
    0. Exit
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Power
    6. Square root
    7. Modulo
    8. Trigonometry
    9. Factorial''')
    choice = input("Enter choice from 0-9 : ")
    if choice in('0','1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if choice in('0'):
            break
        if choice in('1', '2', '3', '4', '5', '7'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} x {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {modulo(num1, num2)}")
        elif choice in('6'):
            num = float(input("Enter the number: "))
            print(f"Square root of {num} is {squareroot(num)}")
        elif choice in ('8'):
            trigonometry()
        elif choice in ('9'):
            num = float(input("Enter the number: "))
            print(f"Factorial of {num} = {factorial(num)}")
        next = input("Continue calculating? (yes/no): ")
        if next == "no":
            break
    else:
     print("Input invalid")