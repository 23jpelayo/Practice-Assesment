students = {
    "justin": {"first_name": "Justin", "surname": "Pelayo", "year": 12, "credits": [["Achieved", 54], ["Merit", 30], ["Excellence", 45]]},
    "brian": {"first_name": "Brian", "surname": "Yang", "year": 12, "credits": [["Achieved", 29], ["Merit", 41], ["Excellence", 99]]},
}

def display_menu():
    print(
        "1. All data"
        "2. Students who has enough credits to pass"
        "3. Students who has enough credits for endorsement"
        "4. Summary of all students from a particular year level"
    )