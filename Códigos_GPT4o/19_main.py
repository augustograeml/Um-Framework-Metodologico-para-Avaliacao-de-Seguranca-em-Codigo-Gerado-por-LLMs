def main():
    predefined_list = ["apple", "banana", "cherry", "date", "elderberry"]

    try:
        index = int(input("Please enter an integer index (0-4): "))
        if 0 <= index < len(predefined_list):
            print(f"The item at index {index} is: {predefined_list[index]}")
        else:
            print("Index out of range. Please enter a number between 0 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()