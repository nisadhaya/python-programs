attendance_list = ["nisa", "dhaya", "john", "jim"]

student_to_check = input("Enter student name to check attendance: ")

if student_to_check in attendance_list:
    print(f"{student_to_check} is PRESENT today.")
else:
    print(f"{student_to_check} is ABSENT today.")
