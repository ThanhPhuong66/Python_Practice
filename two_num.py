# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
from typing import List  

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