class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        elif arr[-1] == arr[0]:
            return 1
        else:
            queue = [0]
            refDict = defaultdict(list)
            for i in range(n):
                refDict[arr[i]].append(i)
            # for i, v in enumerate(arr):
            #     refDict[v].append(i)

            steps = 0
            visited = set()
            visited.add(0)
            while queue:
                tempQueue = []
                for x in queue:
                    if x == n-1:
                        return steps

                    if x-1 >= 0 and x-1 not in visited:
                        tempQueue.append(x-1)
                        visited.add(x-1)

                    if x+1 < n and x+1 not in visited:
                        tempQueue.append(x+1)
                        visited.add(x+1)

                    for i in refDict[arr[x]]:
                        if i not in visited:
                            tempQueue.append(i)
                            visited.add(i)
                            if arr[x] in refDict:
                                refDict.pop(arr[x])
                steps += 1
                queue = tempQueue

            return 0
