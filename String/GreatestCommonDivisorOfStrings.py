class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        tempString = ""
        result = ""
        for i in range(len(str1)):
            tempString += str1[i]
            if len(str1) % (i+1) == 0 and len(str2) % (i+1) == 0:
                if tempString * (len(str1) // (i+1)) == str1 and tempString * (len(str2) // (i+1)) == str2:
                    result = tempString

        return result
