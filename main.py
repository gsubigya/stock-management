from inventory import invoice
from update import greeting, update
from display import display


def main():
    """
    The main function of the program. Displays a greeting, and
    provides options for viewing product list or exiting.
    """

    greeting()  # Display the initial greeting

    while True:  # Main program loop
        print("\nChoose an option:")  # Clearer prompt
        print("1. View product list")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display() 
            elif choice == 0:
                print("Program ended.")
                break  # Exit the loop
            else:
                print("Invalid option. Please choose 0 or 1.")

        except ValueError:
            print("Invalid input. Please enter a number (0 or 1).")


if __name__ == "__main__":
    main()
