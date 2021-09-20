# Approach-1
# Recursive Memoization

class Solution:
    def __init__(self):
        self.dp = {}

    def integerBreak(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        if n == 2:
            return 1
        else:
            ans = -1
            for i in range(2, n):
                firstnumber = i
                secondnumber = n - i
                product = firstnumber * \
                    max(secondnumber, self.integerBreak(secondnumber))
                ans = max(ans, product)
            self.dp[n] = ans
            return ans


# Approach-2
# Tabular DP

class Solution:
    def integerBreak(self, n: int) -> int:
        arr = [0]*(n+1)
        arr[1] = 1
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                temp = max(j, arr[j])*max(i-j, arr[i-j])
                if temp > arr[i]:
                    arr[i] = temp
        return arr[-1]
