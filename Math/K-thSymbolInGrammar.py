class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        total = pow(2, n-1)
        mid = total // 2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            return int(not self.kthGrammar(n-1, k-mid))
