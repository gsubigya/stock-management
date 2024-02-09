from update import update
from inventory import invoice


def display():
    """
    Displays available products, handles customer purchase, updates inventory, and generates an invoice.
    """

    customer_name = input("Enter Customer's Name: ")
    purchase_info = [customer_name]  # Store customer name for invoice

    # Read product data from "data.txt"
    products = []
    with open("data.txt", "r") as data_file:
        print("\nFollowing products are available in our store:\n")
        print("S.No.  Name               Price              Available Pieces")

        for index, line in enumerate(data_file):
            line = line.strip()  # Remove trailing newline
            product_name, price, quantity = line.split(",")
            products.append([product_name, price, quantity])
            print(f"{index + 1}.    {product_name:<15}  {price:<15}  {quantity}")  # Formatted output

    # Get product selection from the user
    while True:
        try:
            serial_number = int(input("\nEnter the Serial No. of desired item: "))
            selected_product = products[serial_number - 1]
            break  # Exit loop if selection is valid
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid Serial No.")

    # Process purchase
    if int(selected_product[2]) > 0:  # Check if the product is in stock
        print("Transaction Succeed!\n")
        selected_product[2] = str(int(selected_product[2]) - 1)  # Decrement quantity
        purchase_info.append(selected_product)  # Add product details for invoice

        update(products)  # Update "data.txt" with new inventory
        invoice(purchase_info)  # Generate invoice
    else:
        print("Sorry! The product you requested is out of stock.")

