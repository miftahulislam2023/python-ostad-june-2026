# Example 8: Calculate difference between two dates
from datetime import date

date1 = date(2026, 12, 31)
date2 = date.today()

difference = date1 - date2
print(f"Days left until December 31, 2026: {difference.days} days")
