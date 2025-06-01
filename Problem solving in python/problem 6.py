"""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function."""


def is_leap(year):
    leap = False
    if (1900 < year < (10*10*10*10*10)):
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return True
        else:
            return leap
    else:
        return leap


year = int(input())
print(is_leap(year))
