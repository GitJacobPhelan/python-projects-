
def addition(a, b):
    result = a + b
    return result

def subtraction(a, b):
    result = a - b
    return result

def division(a, b):
    result = a / b
    return result

def multiplication(a, b):
    result = a * b
    return result

# Main calculator loop
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

        if operation not in ('+','-','/','*'):
            print("Invalid operation.")
            continue

        while True:
            try:
                a = float(input('Enter your first number: '))
                break

            except ValueError:
                print("That is not a valid number.")

        while True:
            try:
                b = float(input('Enter your second number: '))
                if operation == '/' and b == 0:
                    print("Division by 0 not allowed.")
                else:
                    break
            except ValueError:
                print("That is not a valid number.")

        # Arithmetic Functions
        if operation == '+':
            result = addition(a, b)
            print(f"{a} + {b} = {result}")

        elif operation == '-':
            result = subtraction(a, b)
            print(f"{a} - {b} = {result}")

        elif operation == '/':
            result = division(a, b)
            print(f"{a} / {b} = {result}")

        elif operation == '*':
            result = multiplication(a, b)
            print(f"{a} * {b} = {result}")

calculator()

