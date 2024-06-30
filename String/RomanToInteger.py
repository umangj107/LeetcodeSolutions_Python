class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s)==0:
            return 0
        refdict= {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        i=0
        result=0
        while i<len(s)-1:
            if refdict[s[i]]>refdict[s[i+1]] or refdict[s[i]]==refdict[s[i+1]]:
                result+=refdict[s[i]]
                i+=1
            else:
                result+=(refdict[s[i+1]]-refdict[s[i]])
                i+=2
        if i<len(s):
            result+=refdict[s[len(s)-1]]
        
        return result