

import datetime
# A date in Python is not a data type of its own,
# but we can import a module named datetime to work with dates as date objects.

# example to date and time function or module

x = datetime.datetime.now()

print(x.day, x.month, x.year)

# you can create datetime() function

x = datetime.datetime(2022,7,28)
print(x)