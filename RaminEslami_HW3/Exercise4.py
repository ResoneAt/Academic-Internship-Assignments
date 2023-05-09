from datetime import datetime, timedelta
import jdatetime


def seconds_of_life(birthday: datetime) -> float:
    """
    This function takes the date of birt day and returns the age in seconds
    :param birthday: birthday in datetime format
    :return: age in seconds
    """
    age_in_seconds = (datetime.now() - birthday).total_seconds()
    return age_in_seconds


def time_to_next_birthday(birthday: datetime) -> timedelta:
    """
    this function takes the date of birth and returns the amount of time left
    to the birth in timedelta format
    :param birthday: birthday in datetime format
    :return: the amount of time left until birth in timedelta format
    """
    now = datetime.now()
    next_birthday = datetime(now.year, birthday.month, birthday.day)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, birthday.month, birthday.day)
    time_to_birthday = next_birthday - now
    return time_to_birthday


def shamsi_birthday(birthday: datetime) -> str:
    """
    this function converts shamsi to AD
    :param birthday: date of birth in AD
    :return: date of birth in shamsi
    """
    birthday = jdatetime.datetime.fromgregorian(datetime=birthday)
    shamsi = str(birthday.strftime("%Y-%m-%d"))
    return shamsi


def happy_birthday(date_of_birth: str) -> tuple | str:
    """
    This function receives the date of birth and displays the total number of seconds of his life in the output,
    and also calculates the number of days and minutes remaining until the next birthday and congratulates him,
    and also converts and displays the date of birth in shamsi .
    :param date_of_birth: birthday in datetime format
    :return: tuple of age in seconds , days to birthday, minutes of to birthday, congratulates message, shamsi birth
    """
    try:
        birthday = datetime.strptime(date_of_birth, "%Y-%m-%d")
        seconds = seconds_of_life(birthday)
        time_to_birthday = time_to_next_birthday(birthday)
        days_to_birthday = time_to_birthday.days
        minutes_of_to_birthday = int(time_to_birthday.total_seconds() // 60)
        shamsi = shamsi_birthday(birthday)
        message = "Happy birthday in advance"
        return seconds, days_to_birthday, minutes_of_to_birthday, message, shamsi

    except ValueError:
        return 'check your input, You have ValueError... try again'


def main():
    birthday_str = input('enter your birthday (for example 1990-11-28): ')
    self = happy_birthday(birthday_str)
    print(f'hello user ...'
          f'Your age in seconds: {self[0]}\n'
          f'and {self[1]} days and {self[2]} minutes left for your birthday\n'
          f'and i wanted congratulate you in advance, so, {self[3]}\n'
          f'Date of birthday in Hijri: {self[4]}')


if __name__ == "__main__":
    main()
