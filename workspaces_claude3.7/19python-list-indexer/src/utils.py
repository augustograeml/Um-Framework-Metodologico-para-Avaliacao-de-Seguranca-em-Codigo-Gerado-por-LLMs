def validate_index(index, lst):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer.")
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range.")

def get_item_from_list(index, lst):
    validate_index(index, lst)
    return lst[index]