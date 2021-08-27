#Approach-1
#DP-Approach

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_num_steps = [99999 for _ in range(len(nums))]
        min_num_steps[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    min_num_steps[i+j] = min(min_num_steps[i+j],1+min_num_steps[i])

        print(min_num_steps)
        return min_num_steps[-1]


#Approach-2

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        left, right = 0, nums[0]
        answer = 1
        
        # each time find a window of indices that can be reached in 'answer' steps
        while right < len(nums) - 1:
            answer += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, nxt
            
        return answer


#Approach-3
#Efficient-Approach

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        else:
            curr_reach = 0
            max_reach = 0
            jumps = 0
            
            for i in range(n-1):
                max_reach = max(max_reach, i+nums[i])
                
                if i == curr_reach:
                    jumps+=1
                    curr_reach = max_reach
                    
            return jumps    