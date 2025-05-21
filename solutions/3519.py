from collections import defaultdict

class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        # counts[i][color] = how many balls of 'color' player i picked
        counts = [defaultdict(int) for _ in range(n)]
        for player, color in pick:
            counts[player][color] += 1

        winners = 0
        for i in range(n):
            # player i needs at least i+1 balls of the same color
            requirement = i + 1
            # check if any color meets that requirement
            if any(cnt >= requirement for cnt in counts[i].values()):
                winners += 1

        return winners
