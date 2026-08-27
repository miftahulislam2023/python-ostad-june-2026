# Example 7: Date & time arithmetic using timedelta
from datetime import datetime, timedelta

now = datetime.now()

future_date = now + timedelta(days=7)
past_date = now - timedelta(days=30)
future_time = now + timedelta(hours=3, minutes=15)

print("Current Date:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("7 days from now:", future_date.strftime("%Y-%m-%d"))
print("30 days ago:", past_date.strftime("%Y-%m-%d"))
print("3 hours 15 mins from now:", future_time.strftime("%H:%M:%S"))
