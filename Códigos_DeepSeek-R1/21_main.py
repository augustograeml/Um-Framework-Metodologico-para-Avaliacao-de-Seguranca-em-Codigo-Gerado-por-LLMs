def divide_numbers(num1, num2):
    return num1 / num2

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide_numbers(num1, num2)
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()