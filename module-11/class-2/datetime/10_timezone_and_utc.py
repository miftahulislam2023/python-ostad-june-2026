# Example 10: Working with UTC and Timezones
from datetime import datetime, timezone, timedelta

# UTC current time
utc_now = datetime.now(timezone.utc)
print("UTC Time:", utc_now)

# Custom offset (e.g., Bangladesh UTC+6)
bd_timezone = timezone(timedelta(hours=6))
bd_now = datetime.now(bd_timezone)
print("Bangladesh Time (UTC+6):", bd_now)
