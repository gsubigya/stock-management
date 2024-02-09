def greeting():
    """Prints a welcome message for the Stock Management System."""
    print("----WELCOME TO STOCK MANAGEMENT SYSTEM----\n")


def update(list_of_items):
    """Updates the 'data.txt' file with the current inventory data.

    Args:
        list_of_items: A list of lists, where each inner list represents
                       an item with [name, price, quantity] information.
    """

    with open("data.txt", "w") as f:  # Using 'with' for safer file handling
        for item in list_of_items:
            name, price, quantity = item  # Unpacking for readability
            item_data = f"{name},{price},{quantity}\n"
            f.write(item_data)
