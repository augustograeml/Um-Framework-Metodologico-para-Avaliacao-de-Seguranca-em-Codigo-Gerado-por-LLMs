def get_indexed_value(index):
    predefined_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    if 0 <= index < len(predefined_list):
        return predefined_list[index]
    else:
        raise IndexError("Index out of range.")

def main():
    try:
        user_input = int(input("Enter an integer index to access the predefined list: "))
        value = get_indexed_value(user_input)
        print(f"The value at index {user_input} is: {value}")
    except ValueError:
        print("Please enter a valid integer.")
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()