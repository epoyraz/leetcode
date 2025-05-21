class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int  # 1 if p1 wins, 2 if p2 wins, 0 if tie
        """
        def score(arr):
            total = 0
            n = len(arr)
            for i in range(n):
                x = arr[i]
                # check previous two turns
                if (i >= 1 and arr[i-1] == 10) or (i >= 2 and arr[i-2] == 10):
                    total += 2 * x
                else:
                    total += x
            return total

        s1 = score(player1)
        s2 = score(player2)
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0
