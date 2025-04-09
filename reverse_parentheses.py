# The user is given a string s consisting of lowercase English letters and parentheses. The task is to reverse the substrings within each pair of parentheses, starting from the innermost pair. The final result should not contain any parentheses.
# Input: s = "(abcd)"
# Output: "dcba"

#Version 1
class Solution:  
    def reverseParentheses(self, s: str) -> str:  
        stack = []  # Ngăn xếp để lưu trữ chuỗi  
        current_string = ""  # Chuỗi hiện tại  
        # Duyệt từng ký tự trong chuỗi s  
        for char in s:  
            if char == '(':  
                # Khi gặp '(', lưu lại chuỗi hiện tại và bắt đầu một chuỗi mới  
                stack.append(current_string)  
                current_string = ""  # Bắt đầu chuỗi mới bên trong dấu ngoặc  
            elif char == ')':  
                # Khi gặp ')', đảo ngược chuỗi hiện tại  
                current_string = current_string[::-1]  # Đảo ngược chuỗi hiện tại  
                # Ghép với chuỗi đã lưu lại từ ngăn xếp  
                current_string = stack.pop() + current_string  
            else:  
                # Nếu là ký tự thường, thêm vào chuỗi hiện tại  
                current_string += char  
        return current_string  # Trả về chuỗi cuối cùng sau khi xử lý  

solution = Solution()  
print(solution.reverseParentheses("(abcd)"))           
print(solution.reverseParentheses("(ed(et(oc))el)"))  

# Version 2:
class Solution_V2:  
    def reverseParenthesesOptimized(self, s: str) -> str:  
        # Bước 1: Xây dựng bảng vị trí cặp ngoặc  
        stack = []  # Ngăn xếp để lưu các vị trí của dấu ngoặc mở  
        pair = {}   # Dictionary để lưu trữ các vị trí của cặp ngoặc  
        # Duyệt qua từng ký tự trong chuỗi s cùng với chỉ số của nó  
        for i, char in enumerate(s):  
            if char == '(':  # Nếu gặp dấu ngoặc mở  
                stack.append(i)  # Lưu vị trí của dấu ngoặc mở vào ngăn xếp  
            elif char == ')':  # Nếu gặp dấu ngoặc đóng  
                j = stack.pop()  # Lấy vị trí của dấu ngoặc mở từ ngăn xếp  
                # Lưu vị trí cặp ngoặc vào dictionary  
                pair[i] = j  # Vị trí dấu ngoặc đóng (i) tương ứng với dấu ngoặc mở (j)  
        # Bước 2: Duyệt chuỗi với nhảy 2 chiều  
        result = []  # Danh sách để lưu các ký tự đã xử lý  
        i, step = 0, 1  # Bắt đầu chỉ số tại 0 và bước nhảy là 1 (tiến tới)  
        while i < len(s):  # Trong khi chỉ số i nhỏ hơn chiều dài của chuỗi  
            if s[i] == '(' or s[i] == ')':  # Nếu gặp dấu ngoặc  
                i = pair[i]  # Nhảy tới chỉ số của dấu ngoặc tương ứng trong pair  
                step = -step  # Đảo ngược bước (nếu bước đang đi tới thì giờ sẽ đi lùi và ngược lại)  
            else:  # Nếu đây là ký tự thông thường  
                result.append(s[i])  # Thêm ký tự vào danh sách kết quả  
            i += step  # Cập nhật chỉ số i theo bước nhảy  
        return ''.join(result)  # Trả về kết quả dưới dạng chuỗi  

# Ví dụ sử dụng  
solution = Solution_V2()  
print(solution.reverseParenthesesOptimized("(u(love)i)"))