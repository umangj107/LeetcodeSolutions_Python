# Approach-1

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def findMaxConsecutiveOnes(self, nums):
        maxcount = 0
        n = len(nums)

        if 0 not in nums:
            return n

        for i in range(n):
            if nums[i] == 0:
                l = i-1
                r = i+1
                currcount = 1
                while l >= 0 and nums[l] == 1:
                    l -= 1
                    currcount += 1
                while r < n and nums[r] == 1:
                    r += 1
                    currcount += 1
                maxcount = max(maxcount, currcount)

        return maxcount


# Approach-2
# Faster

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        counts = [0 for _ in range(n)]
        flipped = False
        prevzero = -1
        if nums[0] == 0:
            flipped = True
            prevzero = 0
        counts[0] = 1
        for i in range(1, n):
            if nums[i] == 0:
                if not flipped:
                    counts[i] = counts[i-1] + 1
                    flipped = True
                else:
                    counts[i] = counts[i-1] - counts[prevzero] + 1
                prevzero = i
            else:
                counts[i] = counts[i-1] + 1

        print(counts)
        return max(counts)
