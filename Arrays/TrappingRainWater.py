# Approach-1

class Solution:
    def trap(self, height: List[int]) -> int:
        left_highest = [0]
        right_highest = [0]
        n = len(height)
        for i in range(1, n):
            left_highest.append(max(left_highest[-1], height[i-1]))

        for i in range(n-2, -1, -1):
            right_highest.append(max(right_highest[-1], height[i+1]))
        right_highest.reverse()

        result = 0
        for i in range(n):
            res = (min(left_highest[i], right_highest[i]) - height[i])
            if res > 0:
                result += res

        return result


# Approach-2
# Efficient Approach


class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        Lmax = 0
        Rmax = 0
        result = 0

        while L < R:
            if height[L] < height[R]:
                if height[L] >= Lmax:
                    Lmax = height[L]
                else:
                    result += (Lmax - height[L])
                L += 1

            else:
                if height[R] >= Rmax:
                    Rmax = height[R]
                else:
                    result += Rmax - height[R]
                R -= 1

        return result
