#The problem requires calculating the day number of the year based on a given date in the format YYYY-MM-DD.
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.


class Solution:  
    def dayOfYear(self, date: str) -> int:  
        year, month, day = map(int, date.split('-'))  
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
            days_in_month[1] += 1

        return sum(days_in_month[:month-1]) + day  

solution = Solution()  
print(solution.dayOfYear("2019-01-09"))  
print(solution.dayOfYear("2019-02-10")) 