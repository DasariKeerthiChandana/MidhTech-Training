import math
while True:
    print("===== SCIENTIFIC CALCULATOR =====")
    print("+, -, *, /, sqrt, pow, log, sin, cos, tan, fact")
    operator = input("Select an operator: ")
    if operator in ['+', '-', '*', '/', 'pow']:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        if operator == '+':
            print(n1 + n2)
        elif operator == '-':
            print(n1 - n2)
        elif operator == '*':
            print(n1 * n2)
        elif operator == '/':
            if n2 != 0:
                print(n1 / n2)
            else:
                print("Cannot divide by zero.")
        elif operator == 'pow':
            print(math.pow(n1, n2))
    elif operator in ['sqrt', 'log', 'sin', 'cos', 'tan', 'fact']:
        n = float(input("Enter a number: "))
        if operator == 'sqrt':
            print(math.sqrt(n))
        elif operator == 'log':
            if n > 0:
                print(math.log10(n))
            else:
                print("Log is defined only for positive numbers.")
        elif operator == 'sin':
            print(math.sin(math.radians(n)))
        elif operator == 'cos':
            print(math.cos(math.radians(n)))
        elif operator == 'tan':
            print(math.tan(math.radians(n)))
        elif operator == 'fact':
            if n >= 0:
                print(math.factorial(int(n)))
            else:
                print("Factorial is defined only for non-negative integers.")
    else:
        print("Invalid operator!")
    choice = input("Do you want to calculate again? (y/n): ")
    if choice == 'n':
        print("Thank you for using the Scientific Calculator!")
        break