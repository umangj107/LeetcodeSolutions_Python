# Approach-1

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dct = {}
        N = len(pattern)
        s = s.split(" ")
        if N != len(s):
            return False

        for i in range(N):
            if pattern[i] in dct:
                if s[i] != dct[pattern[i]]:
                    return False
            else:
                for k in dct:
                    if dct[k] == s[i]:
                        return False
                dct[pattern[i]] = s[i]

        return True


# Approach-2


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        refDict = {}
        refWords = set()
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in refDict:
                if words[i] != refDict[pattern[i]]:
                    return False

            elif pattern[i] not in refDict and words[i] in refWords:
                return False

            elif pattern[i] not in refDict and words[i] not in refWords:
                refDict[pattern[i]] = words[i]
                refWords.add(words[i])

        return True
