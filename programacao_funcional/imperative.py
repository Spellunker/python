# List all months with 31 days
from calendar import mdays, month_name


print("Months with 31 days")
for month in range(1, 13):
    if mdays[month] == 31:
        print(f"- {month_name[month]}")
