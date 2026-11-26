# Full name: Jubelle Kate Pridas
# Section: IV-BSIT C
# Activity code: P2
# Date: November 27, 2026

from datetime import datetime

import student_utils


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
    # Repeat the current prompt until a valid grade is entered.
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


def main():
    print("P2 Student Grade Report")
    print("Jubelle Kate Pridas | IV-BSIT C")
    grades = enter_grades()

    generated_at = datetime.now()
    print(f"\nReport generated: {generated_at:%Y-%m-%d %H:%M:%S}")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest(grades)}")
    print(f"Lowest: {student_utils.get_lowest(grades)}")
    print(f"Status: {student_utils.get_status(grades)}")


if __name__ == "__main__":
    main()
