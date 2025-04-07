# The user is given a string s consisting of lowercase English letters and parentheses. The task is to reverse the substrings within each pair of parentheses, starting from the innermost pair. The final result should not contain any parentheses.
# Input: s = "(abcd)"
# Output: "dcba"
class Solution:  
    def reverseParentheses(self, s: str) -> str:  
        stack = []    
        current_string = "" 
        for char in s:  
            if char == '(':  
                stack.append(current_string)  
                current_string = ""  
            elif char == ')':    
                current_string = current_string[::-1]  # Đảo ngược chuỗi hiện tại  
                # Ghép với chuỗi đã lưu lại từ ngăn xếp  
                current_string = stack.pop() + current_string  
            else:  
                current_string += char  

        return current_string   


solution = Solution()  
print(solution.reverseParentheses("(abcd)"))           
print(solution.reverseParentheses("(u(love)i)"))        
print(solution.reverseParentheses("(ed(et(oc))el)"))    
print(solution.reverseParentheses("a(bcdefghijkl(mno)p)q")) 