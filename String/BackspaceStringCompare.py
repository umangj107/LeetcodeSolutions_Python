class Solution:
    def formWord(self, word):
        stack = []
        top = -1

        for character in word:
            if character == '#':
                if top != -1:
                    stack.pop(top)
                    top -= 1
            else:
                stack.append(character)
                top += 1
        
        finalWord = ''
        while top >= 0:
            character = stack[top]
            top -= 1
            finalWord = character + finalWord
        
        return finalWord

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.formWord(s) == self.formWord(t)