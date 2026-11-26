# Full name: Jubelle Kate Pridas
# Section: IV-BSIT C
# Activity code: P3
# Date: November 27, 2026


def add_student(students, name_keys):
    name = input("Name to add: ").strip()
    key = name.casefold()
    if not name:
        print("Enter a student name.")
    elif key in name_keys:
        print(f"Duplicate: {name} is already in the list.")
    else:
        # Store the entered spelling in the list and the lookup key in the set.
        students.append(name)
        name_keys.add(key)
        print(f"Added: {name}")


def remove_student(students, name_keys):
    key = input("Full name to remove: ").strip().casefold()
    if key not in name_keys:
        print("Student not found.")
        return

    for name in students:
        if name.casefold() == key:
            students.remove(name)
            name_keys.remove(key)
            print(f"Removed: {name}")
            return


def search_students(students):
    query = input("Full or partial name to search: ").strip().casefold()
    if not query:
        print("Enter a name to search.")
        return

    matches = [name for name in students if query in name.casefold()]
    if matches:
        print("Found: " + ", ".join(sorted(matches, key=str.casefold)))
    else:
        print("No matching students.")


def display_students(students):
    print("Student list:")
    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")


def main():
    students = []
    name_keys = set()
    print("P3 Student Record Manager")
    print("Jubelle Kate Pridas | IV-BSIT C")

    while True:
        print("\n1. Add | 2. Remove | 3. Search | 4. Display all | 5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students, name_keys)
        elif choice == "2":
            remove_student(students, name_keys)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()


# A list keeps its items in order and allows repeated values.
# I use the students list to keep the names as entered and sort them for display.
# A set stores unique items and has no guaranteed order.
# I use the name_keys set to look up names without matching their capitalization.
