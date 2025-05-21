class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        # start at cell 0 â (r,c) = (0,0)
        r, c = 0, 0
        for cmd in commands:
            if cmd == "UP":
                r -= 1
            elif cmd == "DOWN":
                r += 1
            elif cmd == "LEFT":
                c -= 1
            elif cmd == "RIGHT":
                c += 1
            # boundaries guaranteed by problem statement

        # convert back to cell index
        return r * n + c
