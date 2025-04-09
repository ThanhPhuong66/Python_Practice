# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Version 1: Không sử dụng chuỗi
class Solution:
    def isPalindrome_v1(self, x: int) -> bool:
        # Kiểm tra xem số x có phải là số âm không. Nếu x nhỏ hơn 0, nó không thể là số đối xứng.
        if x < 0:
            return False
        # Kiểm tra xem số có kết thúc bằng 0 hay không (trừ 0). Nếu số kết thúc bằng 0 thì số đó không thể là số đối xứng.
        if x % 10 == 0 and x != 0:
            return False
        reversed_num = 0
        while x > reversed_num:
            # Lấy chữ số cuối cùng của x (bằng x % 10) và thêm vào reversed_num sau khi đã nhân với 10 (để đẩy các chữ số đã có sang bên trái).
            reversed_num = reversed_num * 10 + x % 10
            # Cập nhật x bằng cách loại bỏ chữ số cuối cùng (bằng phép chia nguyên x //= 10).
            x //= 10 
            #Vòng lặp này tiếp tục cho đến khi x nhỏ hơn hoặc bằng reversed_num.
        return x == reversed_num or x == reversed_num // 10

sol = Solution()
result = sol.isPalindrome_v1(12321)
print (result)


#Version 2: Sử dụng chuỗi
class SolutionStr:
    def isPalindrome_v2(self, x: int) -> bool:
        # Kiểm tra giá trị âm, vì số âm không phải là số đối xứng  
        if x < 0:
            return False
         # Chuyển đổi số thành chuỗi và so sánh với chuỗi đảo ngược 
        return str(x) == str(x)[::-1] 
     
solution = SolutionStr()
result_v2 = solution.isPalindrome_v2(121)
print(result_v2)
