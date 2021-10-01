class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        x = []
        count = 0
        max = 0
        if l == 0:
            return 0
        if l == 1:
            return 1
        for i in s:
            if i not in x:
                count += 1
                x.append(i)
            else:
                index = x.index(i)
                x = x[index+1:]
                x.append(i)
                count = len(x)

            if max < count:
                max = count
        if max < len(x):
            max = len(x)
        return(max)
