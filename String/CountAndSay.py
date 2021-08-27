class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            s = "11"
            for i in range(3, n+1):
                result = ""
                s = s+'$'
                count = 1
                for j in range(1, len(s)):
                    if s[j] != s[j-1]:
                        result += f"{count}{s[j-1]}"
                        count = 1

                    else:
                        count += 1

                s = result

            return s
