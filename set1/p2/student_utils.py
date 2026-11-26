# Full name: Jubelle Kate Pridas
# Section: IV-BSIT C
# Activity code: P2
# Date: November 27, 2026

PASSING_AVERAGE = 75


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    # Compare the unrounded average with the passing grade.
    if calculate_average(grades) >= PASSING_AVERAGE:
        return "Pass"
    return "Fail"
