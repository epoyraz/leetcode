class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        n = len(colors)
        cnt = 0
        for i in xrange(n):
            if colors[i] != colors[(i-1) % n] and colors[i] != colors[(i+1) % n]:
                cnt += 1
        return cnt
