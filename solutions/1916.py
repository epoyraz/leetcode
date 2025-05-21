class Solution(object):
    def findCenter(self, edges):
        a, b = edges[0]
        c, d = edges[1]
        return a if a == c or a == d else b
