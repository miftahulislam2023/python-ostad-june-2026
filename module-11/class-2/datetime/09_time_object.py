# Example 9: Working with time objects (without date)
from datetime import time

start_time = time(9, 30, 0)   # 09:30:00 AM
end_time = time(17, 0, 0)     # 05:00:00 PM

print("Work starts at:", start_time)
print("Work ends at:", end_time)
print(f"Start hour: {start_time.hour}, minute: {start_time.minute}")
