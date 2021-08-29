class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = 0
        for i in range(len(edges)):
            n = max(n, max(edges[i][0], edges[i][1]))

        indegree = [0 for _ in range(n)]

        for i in edges:
            indegree[i[0]-1] += 1
            indegree[i[1]-1] += 1

        for i in range(n):
            if indegree[i] == n-1:
                return i+1
