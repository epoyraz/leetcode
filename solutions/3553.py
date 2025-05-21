class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        parity = lambda c: ((ord(c[0]) - ord('a')) + (int(c[1]) - 1)) & 1
        return parity(coordinate1) == parity(coordinate2)
