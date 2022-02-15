# Approach-1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isPerm(s1, s2):
            s2Counter = Counter(s2)
            s1Counter = Counter(s1)
            for i in s1Counter:
                if i in s2Counter and s1Counter[i] == s2Counter[i]:
                    continue
                else:
                    return False
            return True

        l = len(s1)
        for i in range(len(s2)-l+1):
            if isPerm(s1, s2[i:i+l]):
                return True

        return False


# Approach-2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = [0] * 26
        s2Map = [0] * 26

        ordA = ord('a')

        window = len(s1)
        for i in range(window):
            s1Map[ord(s1[i]) - ordA] += 1
            s2Map[ord(s2[i]) - ordA] += 1

        if s1Map == s2Map:
            return True

        for i in range(len(s2) - window):
            s2Map[ord(s2[i]) - ordA] -= 1
            s2Map[ord(s2[i+window]) - ordA] += 1

            if s1Map == s2Map:
                return True

        return False


# Approach-3

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Hash = 0
        s2Hash = 0
        window = len(s1)

        for i in s1:
            s1Hash += hash(i)
        for i in range(window):
            s2Hash += hash(s2[i])

        if s1Hash == s2Hash:
            return True

        for i in range(len(s2)-window):
            s2Hash -= hash(s2[i])
            s2Hash += hash(s2[i + window])
            if s1Hash == s2Hash:
                return True

        return False
