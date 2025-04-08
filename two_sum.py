# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
from typing import List  

# Version 1:
class Solution:  
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        num_to_index = {}

        for index, num in enumerate(nums): 
            complement = target - num  
            if complement in num_to_index:  
                return [num_to_index[complement], index]  
            num_to_index[num] = index  
        return [] 


solution = Solution()  
nums = [2,3,5,7,9]  
target = 14
result = solution.twoSum(nums,target)  
print(result) 

#Version 22
class Solution_V2:
    def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:
        # Bước 1: Lưu lại chỉ số ban đầu và sắp xếp mảng
        nums_with_indices = list(enumerate(nums))  # [(0, 3), (1, 3)]
        nums_with_indices.sort(key=lambda x: x[1])  # Sắp xếp theo giá trị

        # Bước 2: Dùng two pointers
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums_with_indices[left][1] + nums_with_indices[right][1]
            if total == target:
                # Trả về chỉ số gốc (không phải vị trí sau khi sắp xếp)
                return [nums_with_indices[left][0], nums_with_indices[right][0]]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []  # Không tìm thấy
    
solution = Solution_V2()  
nums = [2,3,6,7,9]  
target = 12
result = solution.twoSumOptimized(nums,target)  
print(result) 