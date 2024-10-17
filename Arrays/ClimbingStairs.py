class Solution:
    def climbStairs(self, n: int) -> int:
        secLastStep = 1
        lastStep = 2
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            for i in range(2, n):
                waysToReach = secLastStep + lastStep
                secLastStep = lastStep
                lastStep = waysToReach
        return lastStep
        