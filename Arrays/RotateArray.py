# Approach-1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1:
            return
        else:
            for _ in range(k):
                nums.insert(0, nums.pop(-1))


                
#Approach-2
#Efficient

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n<=1 or k%n == 0:
            return 
        else:
            k = k%n
            nums[:k], nums[k:] = nums[n-k:], nums[:n-k]
