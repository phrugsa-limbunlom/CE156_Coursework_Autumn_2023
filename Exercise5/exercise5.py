import numpy as np


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


def write_output_file(students, output_file):
    with open(output_file, 'w') as f:
        print(students, file=f)
    print("Write output file successfully!")
    return


def count_grade_output(output):
    count_first, count_second, count_third, count_failed = 0, 0, 0, 0
    failed_students = []
    for i in range(output.size):
        # print(type(output[i][4]))
        if output[i][4].decode('utf-8') == "first":
            count_first += 1
        elif output[i][4].decode('utf-8') == "second":
            count_second += 1
        elif output[i][4].decode('utf-8') == "third":
            count_third += 1
        elif output[i][4].decode('utf-8') == "failed":
            failed_students.append(output[i][0])
            count_failed += 1
    return count_first, count_second, count_third, count_failed, failed_students


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
