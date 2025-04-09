# In an infinite binary tree where every node has two children, the nodes are labelled in row order.
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
# Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
# Example 1:
#Input: label = 14
#Output: [1,3,4,14]

from typing import List

#Version 1:
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        result = []

        # Bước 1: Tìm tầng (level) của node với label cho trước
        level = 0
        while (1 << level) <= label:  # 2^level <= label
            level += 1

        # Bước 2: Lùi dần từ label về root
        while label > 0:
            result.append(label)

            # Tính min và max của tầng hiện tại
            level_max = (1 << level) - 1      # 2^level - 1
            level_min = (1 << (level - 1))    # 2^(level - 1)
            #tìm mirrored
            label = level_min + level_max - label

            # Lùi lên tầng cha (tầng trên)
            label //= 2
            level -= 1

        # Đảo ngược kết quả vì ta đi từ dưới lên, cần trả về từ root xuống
        return result[::-1]
sol = Solution()
print(sol.pathInZigZagTree(14))  

# Version 2:
class Solution_V2:
    def pathInZigZagTreeOptimized(self, label: int) -> List[int]:
        path = []
        while label >= 1:
            path.append(label)
            level = label.bit_length()  # tầng của node
            level_start = 1 << (level - 1)
            level_end = (1 << level) - 1
            # Tìm node cha dựa trên vị trí mirrored trong tầng
            label = (level_start + level_end - label) // 2

        return path[::-1]
sol = Solution_V2()
print(sol.pathInZigZagTreeOptimized(26))  
