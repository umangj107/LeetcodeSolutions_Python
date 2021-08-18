#Approach-1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return True
        
        left = 0
        right = n-1
        
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left+=1
                    right-=1
            else:
                if not s[left].isalnum():
                    left+=1
                elif not s[right].isalnum():
                    right-=1
        
        return True
    
###########
#Approach-2
#Efficient

class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_list = [i for i in s if i.isalnum()]
        return ("".join(output_list).lower() == "".join(output_list[::-1]).lower())
