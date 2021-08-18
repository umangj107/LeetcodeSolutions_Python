#Approach-1

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        else:
            even_index = 0
            i = 0
            while i < n:
                if nums[i] % 2 == 0:
                    x = nums.pop(i)
                    nums.insert(even_index,x)
                    even_index+=1
                i+=1
                
            return nums
          
          
#Approach-2
#Using two different arrays for even and odd values, and returning the combination of both array

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.extend(odd)
        return even
      
      
#Approach-3
#Most Efficient
#Using Lambda

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums, key=lambda x:x%2)
        return sorted_array
