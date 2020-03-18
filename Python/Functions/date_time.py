# 11/27/2019
# https://docs.python.org/2/library/datetime.html
# https://docs.python.org/3/library/calendar.html
# 
# Date and Time functions in Python3 language
# Generate html calendar 
# Python tutorial 

import datetime
import calendar

# Get current date and time 
# Truncates it into year, month and day
todaysdate = datetime.datetime.now()

currentYear = todaysdate.year
currentMonth = todaysdate.month
currentDay = todaysdate.day

print("Current date and time")
print(f"No Formatting:{todaysdate}")
print(f"Human Readable format\nMonth/Day/Year: {currentMonth}/{currentDay}/{currentYear}\nTime: {todaysdate.hour}:{todaysdate.minute}")

# Create writeable file
f = open('htmlcalendarcode.html', "w+")

#create html calender object and format to appropiate day and year
myhtmlcal = calendar.HTMLCalendar(firstweekday=0)
cal = myhtmlcal.formatmonth(currentYear,currentMonth)

# Save html to file created
f.write(cal)
f.close
print("HTML File in directory above script. Thank you.")
