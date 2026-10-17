def calculate(a, operator, b):
    if operator == "+" or operator == "plus":
        return a + b

    elif operator == "-" or operator == "minus":
        return a - b

    elif operator == "*" or operator == "x" or operator == "times":
        return a * b

    elif operator == "/" or operator == "divided":
        if b == 0:
            return "Cannot divide by zero."
        return a / b

    return "Unknown operator."