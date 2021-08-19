#Approach-1
#Least Efficient

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checker = set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in checker:
                    checker.add(nums1[i])
                    
        return list(checker)
      
      
      
#Approach-2

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        res=set()
        for i in nums2:
            if i in s1 and i not in res:
                res.add(i)
                
        return list(res)
           
      
      
#Approach-3

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

      
      
#Approach-4
#Most Efficient

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)-(set(nums1)-set(nums2)))
        
