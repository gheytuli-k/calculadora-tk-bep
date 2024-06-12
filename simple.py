import zoneinfo
from datetime import datetime

tz = zoneinfo.ZoneInfo("America/New_York")
now = datetime.now(tz)
print("Current time in New York:", now)
