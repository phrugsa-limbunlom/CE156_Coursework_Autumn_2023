import sys
import pandas as pd


def filter_students_by_department(students, department):
    filtered_students = []
    for student in students:
        if student[2].upper() == department.upper():
            filtered_students.append(student)

    # sort students by registration numbers
    for i in range(len(filtered_students)):
        for j in range(i):
            if filtered_students[i][1] >= filtered_students[j][1]:
                filtered_students[i], filtered_students[j] = filtered_students[j], filtered_students[i]

    # no department match
    if len(filtered_students) == 0:
        return

    names = []
    registration_numbers = []
    departments = []

    student_dict = dict()

    for student in filtered_students:
        names.append(student[0])
        registration_numbers.append(student[1])
        departments.append(student[2])

    student_dict["Name"] = names
    student_dict["Registration Number"] = registration_numbers
    student_dict["Department"] = departments

    format_filtered_students = pd.DataFrame(student_dict)

    return format_filtered_students


if __name__ == "__main__":

    while True:
        try:
            file_name = input("Input file name (include extension) : ")
            with open(file_name, 'r') as file:

                print(f"\n{file_name} opened successfully\n")

                student_list = [tuple(line.strip().split(",")) for line in file]

                print(f"All students information : {student_list}\n")

                while True:
                    dep = input("Input department or type 'exit' if want to quit the program: ")

                    if dep == "exit":
                        break

                    filtered_student_list = filter_students_by_department(student_list, dep)

                    # no match department
                    if filtered_student_list is None:
                        print(f"\nThere is no student matching with the {dep} department\n")
                    else:

                        print(f"\nList of students whose departments are {dep.upper()} :\n{filtered_student_list}")

                break
        except FileNotFoundError:
            sys.exit("File can't open : No such file or directory")
