class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for log in logs:
            if log.startswith('..'):
                if steps != 0:
                    steps-=1
            elif log.startswith('.'):
                continue
            else:
                steps+=1
        return steps
        