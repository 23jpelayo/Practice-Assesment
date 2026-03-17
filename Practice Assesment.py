students = {
    "justin": {"first_name": "Justin", "surname": "Pelayo", "year": 12, "credits": [["Achieved", 58], ["Merit", 30], ["Excellence", 48]]},
    "brian": {"first_name": "Brian", "surname": "Yang", "year": 12, "credits": [["Achieved", 29], ["Merit", 41], ["Excellence", 99]]},
    "john": {"first_name": "John", "surname": "Smith", "year": 11, "credits": [["Achieved", 20], ["Merit", 35], ["Excellence", 50]]},
}

def display_menu():
    # display all the actions users can use
    print(
        "1. All data"
        "\n2. Students who has enough credits to pass"
        "\n3. Students who has enough credits for endorsement"
        "\n4. Summary of all students from a particular year level"
        "\n5. Add credits to a student"
        "\n6. Add new student and credit data"
    )

def all_data():
    # display all data
    for student in students.values():
        print(f"Name: {student["first_name"]} {student["surname"]}"
              f"\nYear level: {student["year"]}"
              f"\n{student["credits"][0][0]} Credits: {student["credits"][0][1]}"
              f"\n{student["credits"][1][0]} Credits: {student["credits"][1][1]}"
              f"\n{student["credits"][2][0]} Credits: {student["credits"][2][1]}")
        print()

def check_pass():
    # show who already passed NCEA
    students_passed = []
    for student in students.values():
        total_credits = (student["credits"][0][1] + student["credits"][1][1] + student["credits"][2][1])
        if total_credits >= 60:
            students_passed.append(student)
    
    print("Students who already passed:")
    for student in students_passed:
        print(f"{student["first_name"]} {student["surname"]}")

def check_endorsement():
    # checks if students have enough for NCEA endorsement and display their names
    excellence_endorsed = []
    merit_endorsed = []
    for student in students.values():
        if student["credits"][2][1] >= 50:
            excellence_endorsed.append(f"{student['first_name']} {student['surname']}")
        elif student["credits"][2][1] + student["credits"][1][1] >= 50:
            merit_endorsed.append(f"{student['first_name']} {student['surname']}")

    print("Excellence endorsed:")
    for student in excellence_endorsed:
        print(student)
    print()
    print("Merit endorsed:")
    for student in merit_endorsed:
        print(student)

def student_year_level_summary():
    # display data of all student from a particular year level
    while True:
        try:
            year_level = int(input("Enter Year Level: "))
            for student in students.values():
                if student["year"] == year_level:
                    print(f"Name: {student["first_name"]} {student["surname"]}"
                        f"\nYear level: {student["year"]}"
                        f"\n{student["credits"][0][0]} Credits: {student["credits"][0][1]}"
                        f"\n{student["credits"][1][0]} Credits: {student["credits"][1][1]}"
                        f"\n{student["credits"][2][0]} Credits: {student["credits"][2][1]}")
            break
        except ValueError:
            print("Invalid input. Must be an integer")

display_menu()

while True:
    print("Enter (0) to exit")
    try:
        choice = int(input("Choose action: "))
        if choice in [0, 1, 2, 3, 4, 5, 6]:
            if choice == 1:
                all_data()
            elif choice == 2:
                check_pass()
            elif choice == 3:
                check_endorsement()
            elif choice == 4:
                student_year_level_summary()
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            else:
                break
        else:
            print("Must be one of the options")

    except ValueError:
        print("Invalid input. Must be an integer")