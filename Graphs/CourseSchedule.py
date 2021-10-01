class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [False for _ in range(numCourses)]
        self.order = [False for _ in range(numCourses)]

        def solve(src, adj):
            self.visited[src] = True
            self.order[src] = True

            for node in adj[src]:
                if not self.visited[node]:
                    c = solve(node, adj)
                    if c == True:
                        return True
                elif self.order[node]:
                    return True
            self.order[src] = False
            return False

        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for p in prerequisites:
            adj[p[0]].append(p[1])

        for i in range(numCourses):
            if not self.visited[i]:
                c = solve(i, adj)
                if c:
                    return False
        return True
