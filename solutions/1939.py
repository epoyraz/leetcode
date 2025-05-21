class Solution(object):
    def countPoints(self, points, queries):
        ans = []
        for x, y, r in queries:
            r2 = r * r
            cnt = 0
            for px, py in points:
                if (px - x) ** 2 + (py - y) ** 2 <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans
