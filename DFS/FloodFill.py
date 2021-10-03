class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, r, c, col, newCol):
            if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0 or image[r][c] != col:
                return
            else:
                image[r][c] = newCol
                for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == col:
                        dfs(image, x, y, col, newCol)

        if image[sr][sc] != newColor:
            dfs(image, sr, sc, image[sr][sc], newColor)
        return image
