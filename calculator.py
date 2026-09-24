"""Simple calculator for the Codveda Python Development Internship.

Level 1 - Task 1
Performs addition, subtraction, multiplication, and division.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient of two numbers.

    Raises:
        ValueError: If second_number is zero.
    """
    if second_number == 0:
        raise ValueError("Cannot divide by zero.")
    return first_number / second_number


def get_number(prompt):
    """Read a valid numeric value from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate(first_number, second_number, operation):
    """Perform the selected operation."""
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }

    if operation not in operations:
        raise ValueError("Invalid operation selected.")

    return operations[operation](first_number, second_number)


def main():
    """Run the interactive calculator."""
    print("\n" + "=" * 32)
    print("       SIMPLE CALCULATOR")
    print("=" * 32)

    while True:
        first_number = get_number("\nEnter first number: ")
        second_number = get_number("Enter second number: ")

        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ").strip()

        try:
            result = calculate(first_number, second_number, operation)
            print(f"\nResult: {result:g}")
        except ValueError as error:
            print(f"\nError: {error}")

        again = input("\nDo you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
