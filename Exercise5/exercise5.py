import numpy as np


# a function will be given a file name from a user
# then using the while loop to ask the user to input the name and try to open the file
# if the file name is not correct, it will print out the message and ask the user to input the name again until the file name is correct
# the open the file and read first line in the file to collect a number of student (the first number in the first line) and coursework weight (the second one)
# initialize the numpy array with 4 columns and n rows (n is a number of student collected from the file)
# for loop the remaining line in the file
# each line will be split and collected each student's registration number, student's exam mark, and student's coursework mark
# then using this data to assign as the registration number in the first column,
# the exam mark in the second column,
# and coursework mark in the third column of the initialized numpy array
# for the last column, it will be calculated by the sum of coursework mark multiplied by a percentage of coursework weight
# and exam mark multiplied by the percentage exam weight (exam weight = 100 - coursework weight)
# then return a number of students and the numpy array containing all students data (reg number, exam mark, coursework mark, overall mark)
def read_input_file():
    while True:
        try:
            file_name = input("Input file name (include extension) : ")
            with open(file_name, 'r') as file:
                print(f"{file_name} opened successfully")
                number, coursework_weight = file.readline().split()
                raw_students_data = np.array([[0, 0.0, 0.0, 0.0]] * int(number))
                i = 0
                for line in file:
                    reg_number, exam_mark, coursework_mark = line.strip().split()
                    raw_students_data[i][0] = int(reg_number)
                    raw_students_data[i][1] = float(exam_mark)
                    raw_students_data[i][2] = float(coursework_mark)
                    raw_students_data[i][3] = (float(coursework_mark) * (float(coursework_weight) / 100)) + (
                            float(exam_mark) * ((100 - float(coursework_weight)) / 100))
                    i += 1
                return raw_students_data, number
        except FileNotFoundError:
            print("Incorrect file name!")


# the function receives all students' data (numpy array) and a number of all students (integer) as arguments
# inside the functon, initialize a student data type containing registration number, exam mark, coursework mark, overall mark, and grade
# a number array containing a list of tuples is initialized by for loop a number of all students and assign data type as a student data type
# then for loop a number of students, getting student data from the student lists given by the argument to assign to four variables (regis, exam, coursework, overall)
# passing those four variables to the called function to calculate a grade for each student
# after the function return the grade of each student, create a tuple containing registration number, exam mark, coursework mark, overall mark, and grade
# and assign in to the initialized numpy array
# then use this numpy array to sort by overall mark and return the array that sorted all students
def process_students_mark(students_data, number):
    studType = [('reg_number', int), ('exam_mark', int), ('coursework_mark', int),
                ('overall_mark', int), ('grade', 'S20')]

    students = np.array([(0, 0, 0, 0, '') for _ in range(number)], dtype=studType)

    for m in range(number):
        regis = students_data[m][0]
        exam = round(students_data[m][1])
        coursework = round(students_data[m][2])
        overall = round(students_data[m][3])

        grade = calculate_grade(exam, coursework, overall)

        students[m] = (regis, exam, coursework, overall, grade)

    sorted_students = np.sort(students, order='overall_mark')

    return sorted_students


# the functon receives exam mark (int), coursework mark (int), overall mark (int) as arguments
# then calculate the grade by the criteria given
# if exam mark or over all mark is less than 30, it is failed
# if overall mark is less than 30, it is failed
# if overall mark is greater than 70, it is first class
# if overall mark is in the range of 50-69 (inclusive), it is second class
# if overall mark is in the range of 40-49 (inclusive), it is third class
def calculate_grade(exam, coursework, overall):
    if exam < 30 or coursework < 30:
        return "failed"

    if overall >= 70:
        return "first"
    elif 50 <= overall <= 69:
        return "second"
    elif 40 <= overall <= 49:
        return "third"
    else:
        return "failed"


# the function receives the students numpy array and the name of output file (string) as arguments
# the function will open the file and write the given students numpy array to the file
def write_output_file(students, output_file):
    with open(output_file, 'w') as f:
        print(students, file=f)
    print("Write output file successfully!")


# the function receives the students numpy array as an argument
# then for loop all students and count a number of student who have first class grade, second class grade, third class grade, and failed
# and also retain student registration number who failed
# the return...
# a number of first class grade student,
# a number of second class grade student,
# a number of third class grade student,
# a number of failed student,
# and registration numbers of failed students
def count_grade_output(students):
    count_first, count_second, count_third, count_failed = 0, 0, 0, 0
    failed_students = []
    for i in range(students.size):
        if students[i][4].decode('utf-8') == "first":
            count_first += 1
        elif students[i][4].decode('utf-8') == "second":
            count_second += 1
        elif students[i][4].decode('utf-8') == "third":
            count_third += 1
        elif students[i][4].decode('utf-8') == "failed":
            failed_students.append(students[i][0])
            count_failed += 1
    return count_first, count_second, count_third, count_failed, failed_students


# main function
# call function to read file and collect all students data and number of students
# call function to process student mark by passing students data and number of students as parameters and collect the result of processing students' marks and grades
# call function to write output file by passing output students and file name as parameters
# then print out number of students for all grades and registration number of failed students
if __name__ == "__main__":
    input_students, number_of_students = read_input_file()
    output_students = process_students_mark(input_students, int(number_of_students))
    write_output_file(output_students, "ex5data_out.txt")

    number_of_first_class_students, number_of_second_class_students, number_of_third_class_students, number_of_failed_students, all_failed_students = count_grade_output(
        output_students)

    print(f"Number of students who have first-class marks : {number_of_first_class_students}")
    print(f"Number of students who have second-class marks : {number_of_second_class_students}")
    print(f"Number of students who have third-class marks : {number_of_third_class_students}")
    print(f"Number of students who have failed : {number_of_failed_students}")
    print(f"Students who have failed : {all_failed_students}")
