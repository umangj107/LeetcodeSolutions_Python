class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        result = []

        hashp = sum([hash(ch) for ch in p])
        temp = sum([hash(ch) for ch in s[:lp]])
        if temp == hashp:
            result.append(0)

        for i in range(ls - lp):
            temp += hash(s[i + lp]) - hash(s[i])
            if temp == hashp:
                result.append(i+1)
        return result
