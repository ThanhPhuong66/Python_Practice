# Find all the lonely numbers in an integer array.
# A number is called lonely if it appears only once in the array and its adjacent numbers (x + 1 and x - 1) do not exist in the array.
# The task is to return all lonely numbers in the array. The result can be returned in any order.
# Input: nums = [10,6,5,8]
# Output: [10,8]

from typing import List

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        max_num = 1000000
        count = [0] * (max_num + 2)

        for num in nums:
            count[num] += 1

        lonely_numbers = []

        for num in range(max_num + 1):
            if count[num] == 1:
                if count[num - 1] == 0 and count[num + 1] == 0:
                    lonely_numbers.append(num)

        return lonely_numbers


sol = Solution()
result1 = sol.findLonely([10, 6, 5, 8])
result2 = sol.findLonely([1, 3, 5, 3])

print(result1) 
print(result2)
