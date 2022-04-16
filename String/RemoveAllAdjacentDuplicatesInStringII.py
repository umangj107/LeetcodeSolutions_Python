class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        curr_count = 0
        stack = []

        for c in s:
            if not stack or c != stack[-1][0]:
                stack.append((c, 1))
            else:
                curr_ele, curr_count = stack[-1]
                if curr_count == k-1:
                    while curr_count != 0:
                        stack.pop(-1)
                        curr_count -= 1
                else:
                    stack.append((c, curr_count+1))

        res = ""
        while stack:
            res += stack[-1][0]
            stack.pop(-1)
        return res[::-1]
