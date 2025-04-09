#The problem requires calculating the day number of the year based on a given date in the format YYYY-MM-DD.
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.

# Version 1:

class Solution_V1:  
    def dayOfYear(self, date: str) -> int:  
        # Tách các phần của ngày: năm, tháng, ngày  
        year, month, day = map(int, date.split('-'))  
        # Danh sách số ngày trong mỗi tháng  
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        # Kiểm tra năm nhuận  
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
            days_in_month[1] += 1  # Thêm 1 ngày cho tháng 2 nếu là năm nhuận  
        # Tính số ngày của năm  
        return sum(days_in_month[:month-1]) + day  

solution = Solution_V1()  
print(solution.dayOfYear("2019-01-09"))

#Version 2:

class Solution_V2:
    def dayOfYearOptimized(self, date: str) -> int:  
        year, month, day = map(int, date.split('-'))
        # Danh sách cộng dồn số ngày tính đến đầu mỗi tháng (không tính năm nhuận)
        prefix_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        # Tính số ngày = ngày trong tháng hiện tại + tổng số ngày các tháng trước
        total_day = prefix_days[month - 1] + day
        # Cộng thêm 1 nếu là năm nhuận và tháng > 2
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if month > 2:
                total_day += 1
        return total_day
    
sol = Solution_V2
print(sol.dayOfYearOptimized("2019-02-10"))
