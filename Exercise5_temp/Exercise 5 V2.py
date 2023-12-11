import numpy as np
import pandas as pd

# Function to calculate overall mark and grade
def mark_calculation(exam, coursework, overall):
    # exam_mark = (exam * (100 - weighting)) / 100.0
    # coursework_mark = coursework * weighting
    # overall = exam_mark + coursework_mark

    print("exam ", exam)
    print("coursework ", coursework)
    print("overall ", overall)

    if exam < 30 or coursework < 30:
        grade = "Fail"
    elif overall >= 70:
        grade = "First Class"
    elif 50 <= overall <= 69:
        grade = "Second Class"
    elif 40 <= overall <= 49:
        grade = "Third Class"
    else:
        grade = "Fail"

    print("Grade ", grade)

    return grade


# Get file name from user input
file_name = input("Please enter the file name: ")

# Read the input file and extract information
with open(file_name, 'r') as file:
    # Read the first line which contains the number of students and the percentage coursework weighting
    first_line = file.readline().split()
    num_students = int(first_line[0])
    coursework_weighting = float(first_line[1])

    print("coursework_weighting ",coursework_weighting)

    # Create a 2-dimensional NumPy array
    array1 = np.array([[0, 0.0, 0.0, 0.0]] * num_students)  # num_students is the number of students

    # Read remaining lines, each line contains (in order) a registration number, an exam mark, a coursework mark:
    for i in range(num_students):
        line = file.readline().split()
        reg_number = int(line[0])
        exam = float(line[1])
        coursework = float(line[2])

        overall_mark = (float(coursework) * (float(coursework_weighting) / 100)) + (
                            float(exam) * ((100 - float(coursework_weighting)) / 100))

        # Calculate overall mark and grade

        # Store input values in a row of the array
        array1[i] = [reg_number, exam, coursework, overall_mark]

# Define named data type
dtype = np.dtype(
    [('RegNumber', int), ('ExamMark', float), ('CourseworkMark', float), ('OverallMark', int), ('Grade', 'U15')])

# Make a 1-dimensional array with four integers and one string fields using a named data type.
array2 = np.array([(0, 0.0, 0.0, 0, "")] * num_students, dtype=dtype)

# From the data in each row of the first array the program should generate a tuple containing the student's registration
# number, exam mark, coursework mark and overall mark, all rounded to the nearest integer, and a grade string
# to be calculated
for i in range(num_students):
    reg_number, exam_mark, coursework_mark, overall_mark = array1[i][:4]

    grade = mark_calculation(round(exam_mark), round(coursework_mark), round(overall_mark))

    # store in the corresponding element in the second array
    array2[i] = (reg_number, exam_mark, coursework_mark, overall_mark, grade)


# Generating a version of the second array that is sorted by overall mark and save it to a file.

# Sort array2 by overall mark (ascending)
array2 = np.sort(array2, order='OverallMark')
df = pd.DataFrame(data=array2)
filepath = 'out.csv'
df.to_csv(filepath, index=False)
# Output sorted array2 to a file
# Output file will look like this: RegNumber | ExamMark | CourseworkMark | OverallMark | Grade
output_file = input("Enter the output file name: ")
with open(output_file, 'w') as f:
    np.savetxt(f, array2, fmt='%d %.1f %.1f %d %s', header='RegNumber ExamMark CourseworkMark OverallMark Grade',
               comments='')

# Count and output the number of students with different grades
first_class_count = np.count_nonzero(array2['Grade'] == 'First Class')
second_class_count = np.count_nonzero(array2['Grade'] == 'Second Class')
third_class_count = np.count_nonzero(array2['Grade'] == 'Third Class')
fail_count = np.count_nonzero(array2['Grade'] == 'Fail')

print(f"\nNumber of First Class students: {first_class_count}")
print(f"Number of Second Class students: {second_class_count}")
print(f"Number of Third Class students: {third_class_count}")
print(f"Number of Failures: {fail_count}")

# Output registration numbers and overall mark of first class students
first_class_students = array2[array2['Grade'] == 'First Class'][['RegNumber', 'OverallMark']]
print("\nRegistration numbers of first class students:", first_class_students)
# Output registration numbers and overall mark of students who failed
failed_students = array2[array2['Grade'] == 'Fail'][['RegNumber', 'OverallMark']]
print("\nRegistration numbers of students who failed:", failed_students)
