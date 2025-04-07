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

print(result1)  # Kết quả có thể là [10, 8]
print(result2)  # Kết quả có thể là [1, 5]
