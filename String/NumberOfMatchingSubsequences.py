class Solution:
    def is_sub(self, word, s):
        index = -1
        for ch in word:
            index = s.find(ch, index+1)
            if index == -1:
                return False
        return True

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c = 0
        for word in words:
            if self.is_sub(word, s):
                c += 1

        return c
