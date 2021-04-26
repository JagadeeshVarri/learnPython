# Write a Python program to calculate number of days between two dates.
import datetime
from datetime import date


first_date = date.today()
last_date = date(1998, 9, 2)
print(first_date)
difference =first_date - last_date
print(f"You've Successfully completed {difference.days} days till day")
