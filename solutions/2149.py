class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        a_moves = 0
        b_moves = 0
        n = len(colors)

        i = 0
        while i < n:
            ch = colors[i]
            j = i
            while j < n and colors[j] == ch:
                j += 1
            count = j - i
            if count >= 3:
                if ch == 'A':
                    a_moves += count - 2
                else:
                    b_moves += count - 2
            i = j

        return a_moves > b_moves
