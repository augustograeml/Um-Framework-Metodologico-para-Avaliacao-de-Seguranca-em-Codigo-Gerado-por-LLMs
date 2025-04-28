def main():
    predefined_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    try:
        user_input = int(input("Please enter an integer index to access the predefined list: "))
        print(f"You selected: {predefined_list[user_input]}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except IndexError:
        print("Index out of range! Please enter a number between 0 and {}.".format(len(predefined_list) - 1))

if __name__ == "__main__":
    main()