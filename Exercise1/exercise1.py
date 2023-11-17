from datetime import datetime
from datetime import date


class InvalidBirthDateException(Exception):
    def __init__(self, message):
        super().__init__(message)



def calculate_age(birth_date):
    current_date = datetime.now().date()
    year_difference = current_date.year - birth_date.year

    if current_date.month < birth_date.month or ( current_date.month == birth_date.month and current_date.day < birth_date.day):
        return year_difference - 1

    return year_difference


def is_valid_date(input_date):
    day, month, year = map(int, input_date.split('/'))

    if month < 1 or month > 12:
        print("Month must be between 1 and 12")
        return False

    if day < 1 or day > 31:
        print("Date must be between 1 and 31")
        return False

    if month in (4, 6, 9, 11) and day > 30:
        print("Date must be between 1 and 30")
        return False

    if month == 2 and day > 29:
        print("Date must be between 1 and 29")
        return False

    if year > datetime.now().year:
        print(f"Year must not be longer than {datetime.now().year}")
        return False

    return True


if __name__ == '__main__':
    date_of_birth = input("Please input your date of birth (dd/mm/yyyy) : ")
    valid_date = is_valid_date(date_of_birth)
    if valid_date:
        print(f"Your input date of birth is : {date_of_birth}")
        date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y').date()
        age = calculate_age(date_of_birth)
        today_date = date.today()
        print(f"Your age is : {age}")
        if date_of_birth.day == today_date.day and date_of_birth.month == today_date.month:
            print("Happy birthday")
    else:
        raise InvalidBirthDateException(f"Invalid input date of birth! : {date_of_birth}")
