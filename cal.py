import calendar

from datetime import date

currentDay = date.today().day
currentMonth = date.today().month
currentYear = date.today().year

#print(currentDay)
print(calendar.month(currentYear,currentMonth))