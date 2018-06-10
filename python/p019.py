year = 1900
day = 7
month = 0
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first_sundays = 0

while (year < 2001):
    day += 7
    if (day > days_in_months[month]):
        day -= days_in_months[month]
        month += 1
        if (month == 12):
            month = 0
            year += 1
            if (year % 4 == 0):
                days_in_months[1] = 29
            else:
                days_in_months[1] = 28
    if (day == 1 and year >= 1901):
        first_sundays += 1
print(first_sundays)
