class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] > 0:
                return 1
            else:
                return 0

        else:
            i = 0
            ans = 0
            while i < n:
                start = i
                while start < n and nums[start] == 0:
                    start += 1

                end = start
                count_negative = 0
                start_negative = -1
                end_negative = -1

                while end < n and nums[end] != 0:
                    if nums[end] < 0:
                        count_negative += 1
                        if start_negative == -1:
                            start_negative = end
                        end_negative = end

                    end += 1

                if count_negative == 0 or count_negative % 2 == 0:
                    ans = max(ans, end-start)
                else:
                    ans = max(ans, end - start_negative - 1)
                    ans = max(ans, end_negative - start)

                i = end + 1

            return ans
