import pandas as pd
# validate whether that number (in the range) is prime or not
def is_prime_number(number):
    list_of_number = [2, 3, 5, 7]

    count_prime = 2
    for i in list_of_number:
        if number != i and number % i == 0:
            count_prime += 1

    # if the number has only two dividend, which is 1 and that number itself, it will be prime
    # otherwise it is non-prime number
    return count_prime <= 2


# find all prime numbers in the range between input number1 and input number2
def find_prime_number(num1, num2):
    num1, num2 = int(num1), int(num2)
    if num2 < num1:
        num1, num2 = num2, num1

    # retain all numbers (in the range) that are prime number
    prime_number = [i for i in range(num1, num2 + 1) if is_prime_number(i)]
    return prime_number


# output 10 prime numbers per line
def format_output(prime_list):
    return pd.DataFrame([prime_list[i:i+10] for i in range(0, len(prime_list), 10)]).astype('Int64').to_string(index=False, header=False)


def validate_numeric_number(num1, num2):
    if not str(num1).isnumeric():
        print(f"input number 1 '{num1}' must be numeric")
    if not str(num2).isnumeric():
        print(f"input number 2 '{num2}' must be numeric")


def validate_positive_number(num1, num2):
    is_num1_positive = True
    is_num2_positive = True

    # verify whether input number1 is positive
    # assign number1 flag to true if it is positive
    # otherwise assign to false
    if num1 < 0:
        print(f"input number 1 '{num1}' must be positive")
        is_num1_positive = False

    # verify whether input number2 is positive
    # assign number2 flag to true if it is positive
    # otherwise assign to false
    if num2 < 0:
        print(f"input number 2 '{num2}' must be positive")
        is_num2_positive = False

    # return the output whether these two input numbers are positive or not
    return is_num1_positive and is_num2_positive


if __name__ == '__main__':
    number1 = input("input number 1 : ")
    number2 = input("input number 2 : ")

    try:
        number1 = int(number1)
        number2 = int(number2)

        # verify whether each input number is positive
        # if not, display an error message for that input number
        is_all_positive_numbers = validate_positive_number(number1, number2)

        # find the result of prime numbers if all input numbers are positive
        if is_all_positive_numbers:
            list_of_prime_number = format_output(find_prime_number(number1, number2))
            print(f"A list of all prime numbers is \n{list_of_prime_number}")

    except ValueError as e:
        # verify and display an error message for each input number that is not numeric
        validate_numeric_number(number1, number2)
