# https://leetcode.com/problems/day-of-the-week/
# 1185. Day of the Week

# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day = datetime.datetime(year, month, day)
        
        return day.strftime("%A")

# Without datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        prev_year = year - 1
        days = prev_year * 365 + prev_year // 4 - prev_year // 100 + prev_year // 400
        days += sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1])
        days += day

        if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            days += 1

        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][days % 7]