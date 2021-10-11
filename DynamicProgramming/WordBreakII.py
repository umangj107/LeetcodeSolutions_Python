class Solution:
    def __init__(self):
        self.refDict = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s in self.refDict:
            return self.refDict[s]

        result = []
        for word in wordDict:
            if s[:len(word)] == word:
                if len(s) == len(word):
                    result.append(word)
                else:
                    temp = self.wordBreak(s[len(word):], wordDict)
                    for t in temp:
                        result.append(word + " " + t)

        self.refDict[s] = result
        return result
