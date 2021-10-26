class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            d = [0] * 26
            for j in range(i, len(s)):
                d[ord(s[j]) - 97] += 1
                _max = max(d)
                _min = min([x for x in d if x != 0])

                res += _max - _min

        return res
