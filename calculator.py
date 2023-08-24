ops = ["+", "-", '*', "/", "^"]
operators = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y,
             "^": lambda x, y: x ** y}

operator = input("Enter an operator " + f"{ops}: ")

if operator not in operators:
    print(f"{operator} not a valid operator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


def get_inputs():
    return num1, num2


get_inputs()
results = operators[operator](num1, num2)
print(round(results, 3))
