# Approach-1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = [0]
        left_sum = [0]
        
        #Preparing array for left_sum
        for i in range(len(nums)-1):
            left_sum.append(left_sum[-1] + nums[i])
        
        #Preparing array for right_sum
        for i in range(len(nums)-1, 0, -1):
            right_sum.insert(0,right_sum[0]+nums[i])
        
        #Checking for index for which left_sum == right_sum
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
            
        return -1
      
      
# Approach-2
# Efficient

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            if left_sum == (S-left_sum-nums[i]):
                return i
            left_sum+=nums[i]
            
        return -1
