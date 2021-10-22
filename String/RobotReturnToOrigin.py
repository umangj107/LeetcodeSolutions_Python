# Approach-1

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        L = R = U = D = 0
        for i in moves:
            if i == 'L':
                L += 1
            elif i == 'R':
                R += 1
            elif i == 'U':
                U += 1
            elif i == 'D':
                D += 1

        if U == D and L == R:
            return True
        else:
            return False


# Approach-2

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L")
