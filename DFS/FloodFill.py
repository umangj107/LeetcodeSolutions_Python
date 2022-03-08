class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        queue = [(sr, sc)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        while queue:
            temp = []
            while queue:
                x, y = queue.pop(0)
                image[x][y] = newColor
                visited[x][y] = True
                for r, c in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and image[r][c] == startColor:
                        temp.append((r, c))

            queue = temp

        return image
