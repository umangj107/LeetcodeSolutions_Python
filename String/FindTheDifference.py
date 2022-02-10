# Approach-1

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ref_s = Counter(s)
        ref_t = Counter(t)

        for i in ref_t:
            if not ref_s[i] == ref_t[i]:
                return i


# Approach-2

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in s:
            t = t.replace(i, "", 1)
        return t
