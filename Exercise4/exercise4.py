import sys
import pandas as pd


# the function receives a list of tuples and a string as two argument
# a list of tuples contain the name, department, registration number for each student
# a string is the department name
# the function will filter all students whose the department in a tuple matched to the department argument
# after filtering, the list of filtered students will be sorted by the registration number (ascending) in the tuple
# then convert the list of filtered students to the dictionary
# and then using that dictionary to create a formatted table by using pandas before return it as an output
# if no department in a tuple list matched to the department argument, return None
def filter_students_by_department(students, department):
    filtered_students = []
    for student in students:
        if student[2].upper() == department.upper():
            filtered_students.append(student)

    # sort students by registration numbers
    for i in range(len(filtered_students)):
        for j in range(i):
            if filtered_students[i][1] <= filtered_students[j][1]:
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


#main function
#receives the file name as an input from a user
#if the file name is not correct, display the error message and terminate
#if the file name is correct, open the file and read all lines from the file
#for each line, split the student information (name, department, registration number) with ',' and these attributes will be retained as a list
#create a tuple and convert that list to the tuple, so now having a list of student tuples
#then, use while loop and ask a user to input a department name
#if the use requires to exit from the program, type 'exit' to break the loop (exit the program)
#if the use input a department name, then call a function by passing the list of student tuples and the department name
#if the called function returns None, display message to indicate that no student departments in the list matched to the given department name
#if not print out all students whose departments matched to the given department name
if __name__ == "__main__":

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
                    print(f"\nThere is no student departments in the list matches to the {dep} department\n")
                else:
                    print(f"\nList of students whose departments are {dep.upper()} :\n{filtered_student_list}")


    except FileNotFoundError:
        sys.exit("File can't open : No such file or directory")
