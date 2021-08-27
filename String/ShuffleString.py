# Approach-1

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_s = list(s)
        for i in range(len(s)):
            shuffled_s[indices[i]] = s[i]
        return ''.join(shuffled_s)


# Approach-2
# Efficient-Approach

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dicString = {}
        for element in zip(list(s), indices):
            dicString[element[1]] = element[0]

        stringList = [dicString[i] for i in range(len(indices))]

        return ''.join(stringList)
