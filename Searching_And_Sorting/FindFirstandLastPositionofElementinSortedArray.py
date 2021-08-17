class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        if n == 0 or n == 1 and nums[0] != target:
            return [-1,-1]
        
        result = []
        start = 0
        end = n-1
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
                
        if nums[mid] != target:
            result = [-1,-1]
            return result
        else:
            start = mid
            end = mid
            while end<n and nums[end] == target:
                end+=1
            while start>=0 and nums[start] == target:
                start-=1
                
            result = [start+1, end-1]
            return result
