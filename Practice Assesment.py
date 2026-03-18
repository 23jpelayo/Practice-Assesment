students = {
    "justinpelayo": {"first_name": "Justin", "surname": "Pelayo", "year": 12, "credits": [["Not Achieved", 0],["Achieved", 58], ["Merit", 30], ["Excellence", 48]]},
    "brianyang": {"first_name": "Brian", "surname": "Yang", "year": 12, "credits": [["Not Achieved", 0],["Achieved", 29], ["Merit", 41], ["Excellence", 99]]},
    "johndoe": {"first_name": "John", "surname": "Doe", "year": 11, "credits": [["Not Achieved", 5],["Achieved", 20], ["Merit", 20], ["Excellence", 35]]},
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
    for details in students.values():
        print(f"Name: {details["first_name"]} {details["surname"]}"
              f"\nYear level: {details["year"]}"
              f"\n{details["credits"][0][0]} Credits: {details["credits"][0][1]}"
              f"\n{details["credits"][1][0]} Credits: {details["credits"][1][1]}"
              f"\n{details["credits"][2][0]} Credits: {details["credits"][2][1]}"
              f"\n{details["credits"][3][0]} Credits: {details["credits"][3][1]}")
        print()

def check_pass():
    # show who already passed NCEA
    students_passed = []
    for details in students.values():
        total_credits = (details["credits"][1][1] + details["credits"][2][1] + details["credits"][3][1])
        if total_credits >= 60:
            students_passed.append(details)
    
    print("Students who already passed:")
    for student in students_passed:
        print(f"{student["first_name"]} {student["surname"]}")

def check_endorsement():
    # checks if students have enough for NCEA endorsement and display their names
    excellence_endorsed = []
    merit_endorsed = []
    for student in students.values():
        if student["credits"][3][1] >= 50:
            excellence_endorsed.append(f"{student['first_name']} {student['surname']}")
        elif student["credits"][3][1] + student["credits"][2][1] >= 50:
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
            for details in students.values():
                if details["year"] == year_level:
                    print(f"Name: {details["first_name"]} {details["surname"]}"
                        f"\nYear level: {details["year"]}"
                        f"\n{details["credits"][0][0]} Credits: {details["credits"][0][1]}"
                        f"\n{details["credits"][1][0]} Credits: {details["credits"][1][1]}"
                        f"\n{details["credits"][2][0]} Credits: {details["credits"][2][1]}"
                        f"\n{details["credits"][3][0]} Credits: {details["credits"][3][1]}")
            break
        except ValueError:
            print("Invalid input. Must be an integer")

def add_credits():
    while True:
        student_name = input("Enter student name: ").lower().replace(" ", "")
        if student_name in students:
            break
        else:
            print("Student not found")
    print("Choose credit type:"
          "\n1. Not Achieved"
          "\n2. Achieved"
          "\n3. Merit"
          "\n4. Excellence")
    while True:
        try:
            credit_type = int(input("Enter credit type: "))
            if credit_type in [1, 2, 3, 4]:
                try:
                    credit = int(input("Enter amount of credits: "))
                except ValueError:
                    print("Input must be an integer")
                current_credit = students[student_name]["credits"][credit_type-1][1]
                current_credit += credit
                students[student_name]["credits"][credit_type-1][1] = current_credit
                break
        except ValueError:
            print("Invalid Input. Must be an Integer")
    
def add_new_student():
    first_name = input("Enter first name: ")
    first_name = list(first_name)
    first_name[0] = first_name[0].upper()
    first_name = "".join(first_name)
    surname = input("Enter surname: ")
    surname = list(surname)
    surname[0] = surname[0].upper()
    surname = "".join(surname)
    while True:
        try:
            year_level = int(input("Enter year level: "))
            not_achieved = int(input("Enter Not Achieved credits: "))
            achieved = int(input("Enter Achieved credits: "))
            merit = int(input("Enter Merit credits: "))
            excellence = int(input("Enter Excellence credits: "))
            break
        except:
            print("Must be an integer")
    student_key = first_name.lower().replace(" ","") + surname.lower().replace(" ", "")
    students[student_key] = {"first_name": first_name, "surname": surname, "year": year_level, "credits": [["Not Achieved", not_achieved], ["Achieved", achieved], ["Merit", merit], ["Excellence", excellence]]}



while True:

    display_menu()
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
                add_credits()
            elif choice == 6:
                add_new_student()
            else:
                break
        else:
            print("Must be one of the options")

    except ValueError:
        print("Invalid input. Must be an integer")