# Approach-1

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            dp = [0 for _ in range(n+1)]
            dp[1] = 1
            dp[2] = 1
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

            return dp[-1]


# Approach-2

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            prev_1 = 1
            prev_2 = 1
            prev_3 = 0
            for i in range(3, n+1):
                temp = prev_3 + prev_2 + prev_1
                prev_3 = prev_2
                prev_2 = prev_1
                prev_1 = temp

            return prev_1


# Approach-3

class Solution:
    def tribonacci(self, n: int) -> int:
        T0 = 0
        T1 = 1
        T2 = 1

        Tn = T0
        Tn1 = T1
        Tn2 = T2
        Tn3 = Tn + Tn1 + Tn2

        if n == 0:
            return T0
        if n == 1:
            return T1
        if n == 2:
            return T2
        if n == 3:
            return Tn3
        nt = 3
        while nt <= n:
            Tn3 = Tn + Tn1 + Tn2
            # print (nt, Tn, Tn1, Tn2, Tn3)
            nt += 1
            Tn, Tn1, Tn2 = Tn1, Tn2, Tn3

        return Tn3
