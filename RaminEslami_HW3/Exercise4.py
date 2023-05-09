from datetime import datetime, timedelta
import jdatetime

birthday_str = input()
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

age_in_seconds = (datetime.now() - birthday).total_seconds()

current_date = datetime.now()
next_birthday = datetime(current_date.year, birthday.month, birthday.day)
if next_birthday < current_date:
    next_birthday = datetime(current_date.year + 1, birthday.month, birthday.day)
time_to_birthday = next_birthday - current_date
days_to_birthday = time_to_birthday.days
minutes_of_birthday = int(time_to_birthday.total_seconds() // 60)

shamsi_birthday = jdatetime.datetime.fromgregorian(datetime=birthday)
