# Find all the lonely numbers in an integer array.
# A number is called lonely if it appears only once in the array and its adjacent numbers (x + 1 and x - 1) do not exist in the array.
# The task is to return all lonely numbers in the array. The result can be returned in any order.
# Input: nums = [10,6,5,8]
# Output: [10,8]

from typing import List

# Version 1:  Sử dụng Thuật toán Đếm

class Solution_V1:
    def findLonely(self, nums: List[int]) -> List[int]:
        #Tạo một mảng để đếm số lần xuất hiện của các số
        max_num = 1000000 
        count = [0] * (max_num + 2) # Mảng count để đếm xuất hiện, bao gồm cả số liền kề
        # Đếm số lần xuất hiện của từng số trong mảng
        for num in nums:
            count[num] += 1
        #Tạo danh sách để chứa các số cô đơn
        lonely_numbers = []
        # Kiểm tra điều kiện cô đơn
        for num in range(max_num + 1): # Kiểm tra nếu số này xuất hiện 1 lần
            if count[num] == 1:
                # Kiểm tra nếu số liền kề không tồn tại
                if count[num - 1] == 0 and count[num + 1] == 0:
                    lonely_numbers.append(num)

        return lonely_numbers

sol = Solution_V1()
result1 = sol.findLonely([10, 6, 5, 8])
print(result1) 

# Version 2: Sử dụng HashSet để Kiểm tra Số Độc Nhất  

class Solution_V2:
    def findLonelyOptimized(self, nums: List[int]) -> List[int]:  
        count = {}  
        # Bước 1: Đếm số lần xuất hiện sử dụng dictionary  
        for num in nums:  
            count[num] = count.get(num, 0) + 1  
        # Bước 2: Tạo danh sách để chứa các số cô đơn  
        lonely_numbers = []  
        num_set = set(count.keys())  # Tạo set chứa các số duy nhất để kiểm tra nhanh  
        # Bước 3: Kiểm tra từng số duy nhất trong dictionary  
        for num in num_set:  
            if count[num] == 1:  # Nếu số này xuất hiện đúng một lần  
                # Kiểm tra xem cả hai số liền kề không có mặt  
                if num - 1 not in num_set and num + 1 not in num_set:  
                    lonely_numbers.append(num)  # Thêm số cô đơn vào danh sách  
        # Bước 4: Trả về danh sách các số cô đơn  
        return lonely_numbers  
    
sol = Solution_V2()
result2 = sol.findLonelyOptimized([1, 3, 5, 3])
print(result2)