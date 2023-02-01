from datetime import datetime
from datetime import date
from decimal import ROUND_DOWN

today = datetime.today()

if today.month == 12 and today.day > 25:
    christmas = datetime(today.year+1, 12, 25, 0, 0, 0)
else:
    christmas = datetime(today.year, 12, 25, 0, 0, 0)


if today.date() == christmas.date():
    print("------------------")
    print("Merry Christmas!!!")
    print("------------------")
else:
    timeLeft = christmas - today
    days = timeLeft.days
    seconds = timeLeft.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print("---------------------------------------------------------------")
    print(f"Christmas is in {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds!")
    print("---------------------------------------------------------------")

