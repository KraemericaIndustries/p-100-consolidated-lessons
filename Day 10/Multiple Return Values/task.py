def is_leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        return True
    else: return False

year = int(input("Enter a year to check if it is a leap year: "))
print(f"Is {year} a leap year?: {is_leap_year(year)}")