class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pvisited = set()
        avisited = set()

        def dfs(visited, i, j):
            visited.add((i, j))
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and heights[r][c] >= heights[i][j]:
                    dfs(visited, r, c)

        for i in range(rows):
            dfs(pvisited, i, 0)
            dfs(avisited, i, cols-1)

        for j in range(cols):
            dfs(pvisited, 0, j)
            dfs(avisited, rows-1, j)

        return list(pvisited.intersection(avisited))
