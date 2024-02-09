import datetime
from update import greeting, update  # Not sure if 'update' is needed here


def invoice(purchase_data):
    """Generates an invoice for a customer's purchase and saves it to a file.

    Args:
        purchase_data: A list containing:
            * Customer name (str)
            * Details: A list with product name (str) and price (str)
    """

    customer_name = purchase_data[0]
    product_name = purchase_data[1][0]
    product_price = purchase_data[1][1]
    purchase_time = str(datetime.datetime.now())

    # Create and open invoice file (using 'with' for safer handling)
    with open(f"INVOICES\{customer_name}.txt", "w+") as invoice_file:
        invoice_file.write("         INVOICE         \n")
        invoice_file.write("---------------------------------\n")
        invoice_file.write(f"Customer Name: {customer_name}\n")
        invoice_file.write("---------------------------------\n")
        invoice_file.write(f"Product: {product_name}\n")
        invoice_file.write("---------------------------------\n")
        invoice_file.write(f"Price: {product_price}\n")
        invoice_file.write("---------------------------------\n")
        invoice_file.write(f"Purchase Time: {purchase_time}\n")
        invoice_file.write("---------------------------------\n")
        invoice_file.write("        THANK YOU!       \n")
        invoice_file.write("    Hope to see you soon \n")

    print("Your invoice has been created.")
