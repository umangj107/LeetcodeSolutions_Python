# Approach-1

class Solution:
    def checkRecord(self, s: str) -> bool:
        total_abs = 0
        curr_late = 0

        for i in s:
            if i == 'A':
                total_abs += 1
                if total_abs >= 2:
                    return False
            if i == 'L':
                curr_late += 1
                if curr_late >= 3:
                    return False
            else:
                curr_late = 0

        return True


# Approach-2

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count('A') >= 2 or 'LLL' in s)
