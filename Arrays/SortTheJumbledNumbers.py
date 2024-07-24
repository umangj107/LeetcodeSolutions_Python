class Solution:
    def getNewNumber(self, num, mapping):
        if num == 0:
            return mapping[0]
        newNum = 0
        multiplier = 1
        while num > 0:
            x = num % 10
            num = num // 10
            newNum = (mapping[x] * multiplier) + newNum
            multiplier *= 10
        
        return newNum
        
        
        
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = dict()
        
        for num in nums:
            k = self.getNewNumber(num, mapping)
            x = d.get(k, [])
            x.append(num)
            d[k] = x
        
        result = []
        for k in sorted(d.keys()):
            result.extend(d[k])
        return result
            
        