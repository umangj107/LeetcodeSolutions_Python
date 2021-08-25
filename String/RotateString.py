#Approach-1

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ls = len(s)
        lg = len(goal)
        if ls != lg:
            return False
        else:
            for _ in range(len(s)):
                s = s[1:]+s[:1]
                if s == goal:
                    return True
                
            return False


#Approach-2
#Efficient-Approach

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 0:
            return False
        return goal in (s + s)