# Approach-1

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        sign = 1
        start = 0
        result = 0
        l = len(s)

        while start < l and s[start] == ' ':
            start += 1

        if start < l and (s[start] == '+' or s[start] == '-'):
            sign = -1 if s[start] == '-' else 1
            start += 1

        if start < l and s[start].isalpha():
            return result

        else:
            while start < l and s[start].isdigit():
                digit = int(s[start])
                start += 1
                result = result * 10 + digit

        if sign * result < -pow(2, 31):
            return -pow(2, 31)
        elif sign * result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        return sign * result


# Approach-2

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        signe = 1
        st = ""
        for i in range(len(s)):
            if i == 0 and s[i] == '-':
                signe = -1
                continue
            if i == 0 and s[i] == '+':
                signe = 1
                continue
            if 48 <= ord(s[i]) <= 57:
                st += s[i]
            else:
                break

        if st == "":
            return 0
        if(signe*int(st) > 2**31-1):
            return 2**31-1
        if(signe*int(st) < -2**31):
            return -2**31
        return signe*int(st)
