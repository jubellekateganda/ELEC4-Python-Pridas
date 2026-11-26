# Full name: Jubelle Kate Pridas
# Section: IV-BSIT C
# Activity code: P1
# Date: November 27, 2026

PASSING_AVERAGE = 75


def enter_grades():
    while True:
        try:
            grade_count = int(input("How many grades will you enter? "))
            if grade_count > 0:
                break
        except ValueError:
            pass
        print("Enter a whole number greater than zero.")

    grades = []
    # Advance to the next grade only after accepting a valid number.
    while len(grades) < grade_count:
        try:
            grade = float(input(f"Enter grade {len(grades) + 1}: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                continue
        except ValueError:
            pass
        print("Enter a number from 0 to 100.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    # Use the average before rounding it for display.
    if calculate_average(grades) >= PASSING_AVERAGE:
        return "Pass"
    return "Fail"


def main():
    grades = []
    print("Student Grade Calculator")
    print("Jubelle Kate Pridas | IV-BSIT C")

    while True:
        print("\n1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            # Wait for grades before calling functions that need a nonempty list.
            if not grades:
                print("Enter grades first.")
                continue
            print(f"\nAverage: {calculate_average(grades):.2f}")
            print(f"Highest: {get_highest(grades)}")
            print(f"Lowest: {get_lowest(grades)}")
            print(f"Status: {get_status(grades)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()


# A local variable belongs to the function where it is created.
# For example, the grades list in main() stores the current grades for the menu.
# A global variable is defined outside functions and can be read across the module.
# PASSING_AVERAGE is global, so get_status() can read it when checking the average.
