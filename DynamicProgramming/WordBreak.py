class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        memset = {}

        @lru_cache(None)
        def dfs(start, s):
            if (start, s) in memset:
                return memset[(start, s)]

            if start == n:
                return True
            else:
                for i in range(start+1, n+1):
                    if s[start:i] in words and dfs(i, s):
                        memset[(start, s)] = True
                        return memset[(start, s)]

                memset[(start, s)] = False
                return memset[(start, s)]

        return dfs(0, s)
