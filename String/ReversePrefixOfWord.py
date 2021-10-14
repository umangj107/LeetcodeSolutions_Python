class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = -1
        for j in range(len(word)):
            if word[j] == ch:
                i = j
                break
        if i >= 0:
            return word[:i+1][::-1] + word[i+1:]
        else:
            return word
