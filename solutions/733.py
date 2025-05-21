class Solution(object):
    def floodFill(self, image, sr, sc, color):
        m, n = len(image), len(image[0])
        orig = image[sr][sc]
        if orig == color:
            return image
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr, sc)
        return image
