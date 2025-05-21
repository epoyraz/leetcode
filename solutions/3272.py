class Solution(object):
    def resultGrid(self, image, threshold):
        """
        :type image: List[List[int]]
        :type threshold: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        from collections import defaultdict

        pixel_sum = [[0] * n for _ in range(m)]
        pixel_count = [[0] * n for _ in range(m)]

        def is_valid_region(i, j):
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    for dx, dy in ((0, 1), (1, 0)):
                        nx, ny = x + dx, y + dy
                        if i <= nx < i + 3 and j <= ny < j + 3:
                            if abs(image[x][y] - image[nx][ny]) > threshold:
                                return False
            return True

        for i in range(m - 2):
            for j in range(n - 2):
                if is_valid_region(i, j):
                    total = 0
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            total += image[x][y]
                    avg = total // 9
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            pixel_sum[x][y] += avg
                            pixel_count[x][y] += 1

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if pixel_count[i][j] == 0:
                    result[i][j] = image[i][j]
                else:
                    result[i][j] = pixel_sum[i][j] // pixel_count[i][j]
        return result
