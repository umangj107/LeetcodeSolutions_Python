# Approach-1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        elif len(digits) == 1 and digits[-1] == 9:
            return [1, 0]

        else:
            digits[-1] = 0
            carry = 1
            for i in range(len(digits)-2, -1, -1):
                x = digits[i] + carry
                if x > 9:
                    carry = 1
                    digits[i] = 0
                else:
                    digits[i] = x
                    carry = 0
                    break

            if carry == 1:
                digits.insert(0, 1)

            return digits


# Approach-2
# Efficient-Approach

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                while digits[i] is 9:
                    digits[i] = 0
                    i -= 1
                if i == 0:
                    digits[i] += 1
                    return digits
                if i == -1:
                    digits.insert(0, 1)
                    return digits
                else:
                    digits[i] += 1
                    return digits
