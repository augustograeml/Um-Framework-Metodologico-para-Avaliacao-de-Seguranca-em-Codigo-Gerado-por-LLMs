def validate_expression(expression):
    # Basic validation to check if the expression contains only valid characters
    valid_chars = set("0123456789+-*/(). ")
    if not set(expression).issubset(valid_chars):
        raise ValueError("Invalid characters in expression.")

def format_output(result):
    # Format the output result for better readability
    return f"The result is: {result}"