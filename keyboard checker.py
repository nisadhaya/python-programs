user_input = input("Press any single key on your keyboard: ")

if len(user_input) == 1:
    if user_input.isalpha():
        print(f"'{user_input}' is a Letter.")
    elif user_input.isdigit():
        print(f"'{user_input}' is a Number.")
    else:
        print(f"'{user_input}' is a Special Character/Symbol.")
else:
    print("Please enter only one character at a time!")
