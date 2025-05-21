class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        moves = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3  # skip the next 3 positions, as they get turned to 'O'
            else:
                i += 1
        return moves
