# Approach-1
# DP
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        if n == 0:
            return 0
        elif n == 1:
            return k
        same = []
        diff = []
        total = 0
        same.append(k)
        diff.append(k)

        same.append(k)
        diff.append(k * (k-1))

        total = same[-1] + diff[-1]

        for i in range(2, n):
            same.append(diff[-1])
            diff.append(total * (k-1))
            total = same[-1] + diff[-1]

        return total


# Approach-2
# Enhanced Space Dp

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k*k
        if k == 1:
            return 0

        lo, hi = k, k*k
        for _ in range(n-2):
            lo, hi = hi, (k-1)*hi + (k-1)*lo
        return hi
