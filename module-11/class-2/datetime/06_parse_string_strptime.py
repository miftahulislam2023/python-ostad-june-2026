# Example 6: Parse string to datetime object (strptime)
from datetime import datetime

date_string = "25-12-2026 14:30:00"
date_object = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

print("Parsed DateTime object:", date_object)
print("Extracted Month:", date_object.month)
print("Extracted Day:", date_object.day)
