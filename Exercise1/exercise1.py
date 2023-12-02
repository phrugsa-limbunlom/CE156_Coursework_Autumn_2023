import sys
from datetime import date
from datetime import datetime
import re


#the function receives date of birth (datetime) as an argument
#then calculate an age by date of birth input and current date
#if the date of birth has passed already before the current date
#the return age will be the age of current year
#otherwise it will return the age of previous year since the date of birth has not come yet in the current year
def calculate_age(birth_date):
    current_date = datetime.now().date()
    year_difference = current_date.year - birth_date.year

    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        return year_difference - 1

    return year_difference


#the function receive date of birth (datetime) input as an argument
#then validate the input date is in the correct range of day, month, and year
#if the day is not in the range 1-31,1-30,1-29 for each specified months
#or month is not in the range 1-12
#the function will print out the message
def validate_date(input_date):
    day, month, year = map(int, input_date.split('/'))

    if month < 1 or month > 12:
        print("Month must be between 1 and 12")

    elif day < 1 or day > 31:
        print("Date must be between 1 and 31")

    elif month in (4, 6, 9, 11) and day > 30:
        print("Date must be between 1 and 30")

    elif month == 2 and day > 29:
        print("Date must be between 1 and 29")


#main function
#receive the date of birth input from the user
#verify the date format
#if the format is not correct print out the message
#if the format is correct but the range of date and month is not correct, call the validation function
#if the input year is greater than the current year, print the message to inform the use and exit program
#if all input is appropriate, calculate the age and then print out
#then also print the 'Happy Birthday' message if today is the user's brith day!
if __name__ == '__main__':
    date_of_birth = input("Please input your date of birth (dd/mm/yyyy) : ")
    try:

        date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y').date()

        print(f"Your input date of birth is : {date_of_birth}")

        if date_of_birth.year > datetime.now().year:
            print(f"Year must not be longer than {datetime.now().year}")
            sys.exit()

        age = calculate_age(date_of_birth)
        today_date = date.today()

        print(f"Your age is : {age}")

        if date_of_birth.day == today_date.day and date_of_birth.month == today_date.month:
            print("Happy birthday!!!")

    except ValueError as e:
        print(f"Invalid input date of birth format! : {date_of_birth}")

        # Verify date of birth pattern.
        # If it is dd/mm/yyyy but still having exception error,
        # it will verify the value of each date, month, and year
        date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        if bool(date_pattern.match(date_of_birth)):
            validate_date(date_of_birth)
