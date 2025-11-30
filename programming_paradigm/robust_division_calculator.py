def safe_divide(numerator, denominator):
    # Attempt to convert to float
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Attempt division
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
