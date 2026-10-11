
def addition(a, b):
    result = a + b
    print (f"{a} + {b} = {result}")

def subtraction(a, b):
    result = a - b
    print (f"{a} - {b} = {result}")

def division(a, b):
    result = a / b
    print (f"{a} / {b} = {result}")

def multiplication(a, b):
    result = a * b
    print (f"{a} * {b} = {result}")

def calculator():
    while True:
        operation = input(
            "Choose an operation:\n" \
            "Addition: + \n" \
            "Subtraction: - \n" \
            "Division: / \n" \
            "Multiplication: * \n" \
            "Quit Program: q \n"
        )

        if operation == 'q':
            break

        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))

        if operation == '+':
            addition(a, b)
        elif operation == '-':
            subtraction(a, b)
        elif operation == '/':
            division(a, b)
        elif operation == '*':
            multiplication(a, b)
        else:
            print('Operation not found.')
            
calculator()

