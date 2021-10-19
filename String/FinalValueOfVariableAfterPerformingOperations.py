# Approach-1

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if operation[1] == '+':
                X += 1
            else:
                X -= 1
        return X


# Approach-2

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        y = 0
        x = ""
        x = x.join(operations).replace("X", "")
        return int((x.count('+') - x.count('-'))/2)
