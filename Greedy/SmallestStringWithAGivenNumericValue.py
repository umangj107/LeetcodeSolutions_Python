# Approach-1
# With Extra Space

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['' for _ in range(n)]
        for i in range(n):
            res[i] = 'a'
            k -= 1

        index = n-1
        while k > 0 and index >= 0:
            if k >= 25:
                res[index] = 'z'
                k -= 25
                index -= 1
            else:
                res[index] = chr(ord(res[index]) + k)
                break

        return ''.join(res)


# Approach-2
# Without Extra Space


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if k == n:
            return 'a'*n

        if k // 26 == n and k % 26 == 0:
            return 'z'*n

        newK = k - n
        zCount = newK // 25
        freeChar = newK % 25

        return 'a'*(n - zCount - 1) + chr(ord('a') + freeChar) + 'z'*zCount
