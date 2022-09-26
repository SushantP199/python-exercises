# import time
#
# print(time.localtime())
#
# print(time.asctime(time.localtime()))

import calendar

calendar.Calendar()

days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')

day1 = calendar.weekday(1947,8,15)
day2 = calendar.weekday(1776,7,4)

output = f"""
The day {days[day1]} on date 15 AUGUST 1947
The day {days[day2]} on date 4 JULY 1776
"""

print(output)

#print(days[calendar.weekday(2000,6,4)])