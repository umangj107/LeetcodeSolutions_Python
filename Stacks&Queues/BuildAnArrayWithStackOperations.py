class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        input = 1
        for i in target:
            while input < i:
                result.append("Push")
                result.append("Pop")
                input+=1
            result.append("Push")
            input+=1
            
        return result
