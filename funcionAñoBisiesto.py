def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):

    if month < 1 or month > 12:
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return days[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None

    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None

    total_days = 0

    for m in range(1, month):
        total_days += days_in_month(year, m)

    return total_days + day


print(day_of_year(2000, 12, 31))
