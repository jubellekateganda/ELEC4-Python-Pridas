# Full name: Jubelle Kate Pridas
# Section: IV-BSIT C
# Activity code: P4
# Date: November 27, 2026

from math import isfinite


def divide_numbers():
    try:
        numerator = float(input("Numerator: "))
        denominator = float(input("Denominator: "))
        if not isfinite(numerator) or not isfinite(denominator):
            raise ValueError("Inputs must be finite numbers.")
        result = numerator / denominator
    except ValueError:
        print("Invalid number. Enter finite numeric values.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
    finally:
        # This message runs after either a successful or failed attempt.
        print("Division attempt finished.")


def open_file():
    file_name = input("File name or path: ").strip()
    try:
        with open(file_name, encoding="utf-8") as source:
            contents = source.read()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except UnicodeError:
        print("Cannot display this file as UTF-8 text.")
    except (OSError, ValueError) as error:
        print(f"Cannot open the file: {error}")
    else:
        print("File contents:")
        print(contents)


def main():
    print("P4 Safe Menu Program")
    print("Jubelle Kate Pridas | IV-BSIT C")

    try:
        while True:
            print("\n1. Divide | 2. Open file | 3. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                divide_numbers()
            elif choice == "2":
                open_file()
            elif choice == "3":
                break
            else:
                print("Invalid menu choice. Choose 1, 2, or 3.")
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended.")

    print("Goodbye!")


if __name__ == "__main__":
    main()
