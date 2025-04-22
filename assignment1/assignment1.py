# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String


def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
def calc(a, b, c="multiply"):
    try:
        if c == "add":
            return a + b
        elif c == "subtract":
            return a - b
        elif c == "multiply":
            return a * b
        elif c == "divide":
            return a / b
        elif c == "modulo":
            return a % b
        elif c == "int_divide":
            return a // b
        elif c == "power":
            return a ** b
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("You can't multiply those values!")

# pytest -v -x assignment1-test.py
# can use just -x, adding -v lists the passing tests
