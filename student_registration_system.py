student_list = []


def create_student():
    name = input("Please enter the new student's name: ")

    student_data = {
        "name": name,
        "marks": []
    }

    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    count_marks = len(student['marks'])
    if count_marks == 0:
        return 0

    total = sum(student['marks'])
    return total / count_marks


def print_student_details(student):
    print(f"{student['name']}, average mark: {calculate_average_mark(student)}")


def print_student_list(students):
    for i, student in enumerate(students):
        print(f"ID: {i}")
        print_student_details(student)


def menu():
    selection =  input("Enter 'p' to print the student list,"
                        "'s' to add a new student,"
                        "'a' to a mark to a student,"
                        "'q' to quit."
                        "Enter your selection: ").lower()

    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student id to add a mark to: "))
            student = student_list[student_id]
            numbers_marks = int(input("Enter the numbers of marks you add: "))
            for i in range(numbers_marks):
                new_mark = int(input(f"Enter the new mark number {i + 1}, to be added: "))
                add_mark(student, new_mark)

        selection = input("Enter 'p' to print the student list,"
                        "'s' to add a new student,"
                        "'a' to a mark to a student,"
                        "'q' to quit."
                        "Enter your selection: ").lower()

menu()
