import datetime
import json

# Load the public holiday data from the JSON file
with open("holidays2025.json", "r") as f:
    holidays = json.load(f)


def is_holiday(date):
    """
    Check if a given date is a public holiday.
    """
    for holiday in holidays:
        if (
            date.date()
            == datetime.datetime.strptime(holiday["date"], "%Y-%m-%d").date()
        ):
            context = {
                "holiday_name": holiday["holiday_name"],
                "holiday_date": holiday["date"],
            }
            return context
    return False


def is_leap_year(year):
    """
    Check if a given year is a leap year.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_weekend(date):
    """
    Check if a given date is a weekend (Saturday or Sunday).
    """
    return date.weekday() in [5, 6]  # Saturday (5) and Sunday (6)


def calculate_project_end_date(start_date, working_days):
    """
    Calculate the project end date based on the start date and the number of working days.
    """
    end_date = start_date
    days_counted = 0

    while days_counted < working_days:
        end_date += datetime.timedelta(days=1)
        holiday = is_holiday(end_date)
        if not is_weekend(end_date) and not is_holiday(end_date):
            days_counted += 1
        elif holiday is not False:
            print(f"Holiday: {holiday['holiday_name']} - {holiday['holiday_date']}")
    return end_date

# Prompt the user for the project start date and the number of working days
while True:
    start_date_str = input("Enter the project start date (YYYY-MM-DD): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

while True:
    working_days = input("Enter the number of working days: ")
    if working_days.isdigit() and int(working_days) > 0:
        working_days = int(working_days)
        break
    else:
        print(
            "Invalid input. Please enter a positive integer for the number of working days."
        )

# Calculate the project end date
end_date = calculate_project_end_date(start_date, working_days)

# Handle leap years
if is_leap_year(start_date.year) and start_date.month == 2 and start_date.day == 29:
    end_date += datetime.timedelta(days=1)

print(f"Project start date: {start_date.date()}")
print(f"Project end date: {end_date.date()}")
