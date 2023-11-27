from datetime import date
from datetime import datetime
import re


def calculate_age(birth_date):
    current_date = datetime.now().date()
    year_difference = current_date.year - birth_date.year

    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        return year_difference - 1

    return year_difference


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

    elif year > datetime.now().year:
        print(f"Year must not be longer than {datetime.now().year}")


if __name__ == '__main__':
    date_of_birth = input("Please input your date of birth (dd/mm/yyyy) : ")
    try:

        date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y').date()

        print(f"Your input date of birth is : {date_of_birth}")

        age = calculate_age(date_of_birth)
        today_date = date.today()

        print(f"Your age is : {age}")

        if date_of_birth.day == today_date.day and date_of_birth.month == today_date.month:
            print("Happy birthday")

    except ValueError as e:
        print(f"Invalid input date of birth format! : {date_of_birth}")

        # Verify date of birth pattern.
        # If it is dd/mm/yyyy but still having exception error,
        # it will verify the value of each date, month, and year
        date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        if bool(date_pattern.match(date_of_birth)):
            validate_date(date_of_birth)
