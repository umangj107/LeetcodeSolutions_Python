from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in paths:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        res = [0 for _ in range(n)]

        for node in range(1, n+1):
            colors = [0 for _ in range(5)]
            for child in graph[node]:
                colors[res[child-1]] = 1
            for c in range(1, 5):
                if colors[c] == 0:
                    res[node-1] = c
                    break

        return res
