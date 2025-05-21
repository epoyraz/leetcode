class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        def position(ch):
            idx = ord(ch) - ord('a')
            return divmod(idx, 5)  # (row, col)

        res = []
        cur_r, cur_c = 0, 0

        for ch in target:
            target_r, target_c = position(ch)

            # Move UP and LEFT before DOWN and RIGHT to handle 'z' correctly
            # Special care for 'z' at (5, 0) since itâs the only char in its row
            while cur_r > target_r:
                res.append('U')
                cur_r -= 1
            while cur_c > target_c:
                res.append('L')
                cur_c -= 1
            while cur_r < target_r:
                res.append('D')
                cur_r += 1
            while cur_c < target_c:
                res.append('R')
                cur_c += 1

            res.append('!')

        return ''.join(res)
