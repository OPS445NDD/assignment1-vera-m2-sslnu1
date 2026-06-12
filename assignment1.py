#!/usr/bin/env python3



"""

Assignment 1 Version A

OPS445



This script calculates the number of weekend days between two dates.



Name: sslnu1



Academic Honesty:

I declare that this assignment is my own work in accordance with Seneca's

Academic Integrity Policy.

"""



import sys





def leap_year(year: int) -> bool:

    """Return True if the year is a leap year."""

    if year % 400 == 0:

        return True



    if year % 100 == 0:

        return False



    if year % 4 == 0:

        return True



    return False





def mon_max(month: int, year: int) -> int:

    """Return the maximum number of days in a given month."""

    if month == 2:

        if leap_year(year):

            return 29

        return 28



    days_in_month = {

        1: 31,

        3: 31,

        4: 30,

        5: 31,

        6: 30,

        7: 31,

        8: 31,

        9: 30,

        10: 31,

        11: 30,

        12: 31

    }



    return days_in_month[month]





def after(date: str) -> str:
    """
    Return the date for the next day in YYYY-MM-DD format.
    """
    str_year, str_month, str_day = date.split('-')

    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month

    return f"{year}-{to_month:02}-{to_day:02}"


def day_of_week(date: str) -> str:
    """
    Return day of week for a date in YYYY-MM-DD format.
    """
    year, month, day = date.split('-')
    year = int(year)
    month = int(month)
    day = int(day)

    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    day_number = (day + ((13 * (month + 1)) // 5) + k + (k // 4) +
                  (j // 4) + (5 * j)) % 7

    days = {
        0: 'Sat',
        1: 'Sun',
        2: 'Mon',
        3: 'Tue',
        4: 'Wed',
        5: 'Thu',
        6: 'Fri'
    }

    return days[day_number]


def valid_date(date: str) -> bool:
    """Return True if the date is valid YYYY-MM-DD format."""
    if len(date) != 10:
        return False

    if date[4] != '-' or date[7] != '-':
        return False

    year_str, month_str, day_str = date.split('-')

    if not year_str.isdigit():
        return False

    if not month_str.isdigit():
        return False

    if not day_str.isdigit():
        return False

    year = int(year_str)
    month = int(month_str)
    day = int(day_str)

    
    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True


def before(date1: str, date2: str) -> bool:
    """Return True if date1 is earlier than date2."""
    year1, month1, day1 = date1.split('-')
    year2, month2, day2 = date2.split('-')

    date1_tuple = (int(year1), int(month1), int(day1))
    date2_tuple = (int(year2), int(month2), int(day2))

    return date1_tuple < date2_tuple


def day_count(start_date: str, end_date: str) -> int:
    """Count Saturdays and Sundays from start_date to end_date inclusive."""
    weekend_count = 0
    current_date = start_date

    while current_date != after(end_date):
        current_day = day_of_week(current_date)

        if current_day == 'Sat' or current_day == 'Sun':
            weekend_count += 1

        current_date = after(current_date)

    return weekend_count


def usage():
    """Print a usage message and exit the program."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    date1 = sys.argv[1]
    date2 = sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()

    if before(date2, date1):
        start_date = date2
        end_date = date1
    else:
        start_date = date1
        end_date = date2

    weekends = day_count(start_date, end_date)

    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")
