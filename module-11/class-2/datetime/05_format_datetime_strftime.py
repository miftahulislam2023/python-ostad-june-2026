# Example 5: Format datetime to string (strftime)
from datetime import datetime

now = datetime.now()

formatted_1 = now.strftime("%Y-%m-%d %H:%M:%S")
formatted_2 = now.strftime("%A, %d %B %Y (%I:%M %p)")

print("Format 1 (Standard):", formatted_1)
print("Format 2 (Readable):", formatted_2)
