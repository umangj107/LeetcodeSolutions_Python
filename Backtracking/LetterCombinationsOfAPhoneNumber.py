class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        self.refDict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.res = set()

        def backtrack(digits, curr_key, pattern):
            if curr_key == len(digits):
                self.res.add(pattern)
                return
            x = self.refDict[digits[curr_key]]
            for i in x:
                pattern += i
                backtrack(digits, curr_key+1, pattern)
                pattern = pattern[:-1]

        backtrack(digits, 0, "")
        return self.res
