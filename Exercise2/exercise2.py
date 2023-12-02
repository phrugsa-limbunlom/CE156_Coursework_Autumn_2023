import pandas as pd

#the function receives a number (integer) as an argument
#validate whether the number is prime or not
#the condition for a prime number is having only two divisors,which is 1 and that number itself
#otherwise it is non-prime number
#the function will return a boolean (True or False) by checking whether the number having only two divisors or not
def is_prime_number(number):
    list_of_number = [2, 3, 5, 7]

    divisors = 2
    for i in list_of_number:
        if number != i and number % i == 0:
            divisors += 1

    return divisors <= 2

#the function receives two arguments as the range of a list of number
#if the input number2 is greater than input number1, the position will be switched before processing to the for loop
#it will find all prime numbers in the range between input number1 and input number2 by calling another function to validate prime number
#if that number is prime, it will be retained in the list
#then the function will return the list of prime numbers
def find_prime_number(num1, num2):
    num1, num2 = int(num1), int(num2)
    if num2 < num1:
        num1, num2 = num2, num1

    prime_number = [i for i in range(num1, num2 + 1) if is_prime_number(i)]
    return prime_number


#the function will receive a list of prime number (list of integer) as an argument
#then return 10 prime numbers per line as a table format using pandas
#by using pandas, it will construct the 2-D arrays with 10 numbers per line as a column and each consecutive subset as a row
#then convert data type to Integer and convert dataframe to string by removing row index and column index
def format_output(prime_list):
    return pd.DataFrame([prime_list[i:i+10] for i in range(0, len(prime_list), 10)]).astype('Int64').to_string(index=False, header=False)


#the function receives input number1 (integer) and number2 (integer) as an argument
#then validate whether the inputs are numeric or not
#if not, print out the message
def validate_numeric_number(num1, num2):
    if not str(num1).isnumeric():
        print(f"input number 1 '{num1}' must be numeric")
    if not str(num2).isnumeric():
        print(f"input number 2 '{num2}' must be numeric")


#the function receives input number1 (integer) and number2 (integer) as an argument
#verify whether input number1 is positive
#assign number1 flag to true if it is positive
#otherwise assign to false
#then verify whether input number2 is positive
#assign number2 flag to true if it is positive
#otherwise assign to false
#after validate two inputs, return boolean (True or False) whether that two input numbers are both positive or not
def validate_positive_number(num1, num2):
    is_num1_positive = True
    is_num2_positive = True

    if num1 < 0:
        print(f"input number 1 '{num1}' must be positive")
        is_num1_positive = False

    if num2 < 0:
        print(f"input number 2 '{num2}' must be positive")
        is_num2_positive = False

    # return the output whether these two input numbers are positive or not
    return is_num1_positive and is_num2_positive


#main function
#receives two input numbers from the user
#verify if each input number is numeric by calling numeric validation function
#if it is non-numeric, display an error message of that number
#if both inputs are numeric, then verify whether each input number is positive or not by calling positive validation function
#if not, display an error message for the input number that is not positive
#if both numbers are positive, proceed to find prime numbers from all numbers in the range between input number1 and input number2
#then display all prime numbers in the list

if __name__ == '__main__':
    number1 = input("input number 1 : ")
    number2 = input("input number 2 : ")

    try:
        number1 = int(number1)
        number2 = int(number2)

        is_all_positive_numbers = validate_positive_number(number1, number2)

        if is_all_positive_numbers:
            list_of_prime_number = format_output(find_prime_number(number1, number2))
            print(f"A list of all prime numbers is \n{list_of_prime_number}")

    except ValueError as e:
        validate_numeric_number(number1, number2)
