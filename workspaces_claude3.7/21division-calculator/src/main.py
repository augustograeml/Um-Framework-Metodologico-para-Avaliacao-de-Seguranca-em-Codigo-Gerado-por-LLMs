def divide(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return numerator / denominator

def main():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = divide(num1, num2)
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()