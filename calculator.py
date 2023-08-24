ops = ["+", "-", '*', "/", "^"]  # allowed operators
# operator functionality
operators = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y,
             "^": lambda x, y: x ** y}

operator = input("Enter an operator " + f"{ops}: ")  # operator input

# operator validity check
if operator not in operators:
    print(f"{operator} not a valid operator")

# number 1, number 2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# returns the number values
def get_inputs():
    return num1, num2


# calculation
get_inputs()
results = operators[operator](num1, num2)
print(round(results, 3))
