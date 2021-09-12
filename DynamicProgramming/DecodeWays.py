class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):
            onedigit = int(s[i-1:i])
            twodigits = int(s[i-2:i])
            print(onedigit)
            print(twodigits)
            if onedigit >= 1:
                dp[i] += dp[i-1]
            if twodigits >= 10 and twodigits <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
