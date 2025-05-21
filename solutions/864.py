class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

        counter = {}
        for (i1, j1) in ones1:
            for (i2, j2) in ones2:
                delta = (i2 - i1, j2 - j1)
                counter[delta] = counter.get(delta, 0) + 1

        return max(counter.values() or [0])
