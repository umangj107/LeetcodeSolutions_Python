# Approach-1

class Solution:
    def reverseWords(self, s: str) -> str:
        def revWord(word):
            wordList = list(word)
            l = 0
            r = len(wordList) - 1
            while l < r:
                wordList[l], wordList[r] = wordList[r], wordList[l]
                l += 1
                r -= 1
            return ''.join(wordList)

        sentence = s.split(' ')
        for i in range(len(sentence)):
            sentence[i] = revWord(sentence[i])

        return ' '.join(sentence)


# Approach-2
# Faster Approach
class Solution:
    def reverseWords(self, s: str) -> str:
        return (' '.join(reversed(s[::-1].split(' '))))
