class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 1:
            pass
        else:
            left = 0
            right = len(s)-1
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
