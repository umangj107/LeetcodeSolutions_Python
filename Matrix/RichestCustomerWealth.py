# Approach-1

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        for i in range(len(accounts)):
            s = 0
            for j in range(len(accounts[0])):
                s = s + accounts[i][j]
            sum_list.append(s)
        res = max(sum_list)
        return res


# Approach-2
# One-line

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)
