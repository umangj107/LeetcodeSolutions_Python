class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        num = (len(rolls) + n) * mean - sum(rolls)
        if num > n * 6 or num < n:
            return []
        if num % n <= 6:
            first = num // n
            last = num - first * (n-1)
            return [first] * (n - 1) + [last]
        else:
            carry = num - (num // n) * (n-1) - 6
            first = num // n
            middle = first + 1
            last = num - first * (n - 1 - carry) - middle * carry
            return [first] * (n - 1 - carry) + [middle] * carry + [last]
