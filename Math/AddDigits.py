# Approach-1

class Solution:
    def addDigits(self, num: int) -> int:
        if num % 10 == num:
            return num
        tempSum = 0
        while num > 0:
            tempSum += (num % 10)
            num = num // 10
        return self.addDigits(tempSum)


# Approach-2

class Solution:
    def addDigits(self, num: int) -> int:
        while(num > 9):
            sum = 0
            r = num % 10
            num = num//10
            sum = sum+r+num
            num = sum
        return num
