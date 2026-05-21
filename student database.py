
student_database = {}
def add_student(roll_no, name):
    student_database[roll_no] = name
    print(f"Added {name} (Roll No: {roll_no}) successfully!")
add_student("101", "nisa")
add_student("102", "dhaya")
add_student("103", "nisha")
print("\n--- STUDENT DATABASE records ---")
for roll, name in student_database.items():
    print(f"Roll No: {roll} | Name: {name}")
