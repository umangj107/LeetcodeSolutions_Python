from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = 0
        refDict = Counter(t)
        count = len(refDict)
        res = s + "-"
        resLen = 9999
        n = len(s)

        while end < len(s):
            if s[end] in refDict:
                refDict[s[end]] -= 1
                if refDict[s[end]] == 0:
                    count -= 1

            if count == 0:
                if len(s[start:end+1]) < len(res):
                    res = s[start:end+1]
                while count == 0:
                    if s[start] in refDict:
                        refDict[s[start]] += 1
                        if refDict[s[start]] == 1:
                            count += 1
                    start += 1
                    if count == 0 and len(s[start:end+1]) < len(res):
                        res = s[start: end+1]

            end += 1

        if len(res) == n+1:
            return ""
        return res
