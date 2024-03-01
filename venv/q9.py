from datetime import datetime

def days_since_birthday(birthday):
    """
    :param birthday: Birthday in the format "DD-MM-YYYY"
    :return: Number of days passed
    """
    # we get  the birthday string to a datetime object
    birth_date = datetime.strptime(birthday, "%d-%m-%Y")

    # get the current date
    current_date = datetime.now()

    # ddjust the birth date to the current year
    adjusted_birth_date = birth_date.replace(year=current_date.year)

    # calculate the difference in days between the adjusted birth date and the current date
    days_passed = (current_date - adjusted_birth_date).days

    return days_passed

# Example usage:
birthday = "29-09-2003"
result = days_since_birthday(birthday)
print(f"Days passed since birthday: {abs(result)} days")