class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = set()

        def backtrack(s, pattern, k):
            if len(pattern) == len(s):
                self.res.add(pattern)
                return
            else:
                if s[k].isalpha():
                    ob1 = pattern + s[k].lower()
                    ob2 = pattern + s[k].upper()
                else:
                    ob1 = ob2 = pattern + s[k]

                backtrack(s, ob1, k+1)
                backtrack(s, ob2, k+1)

        backtrack(s, "", 0)
        return list(self.res)
