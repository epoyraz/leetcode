class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        lsum = rsum = 0
        lq = rq = 0
        for i, ch in enumerate(num):
            if ch == '?':
                if i < half: lq += 1
                else:        rq += 1
            else:
                if i < half: lsum += int(ch)
                else:        rsum += int(ch)

        total_q = lq + rq
        # If odd number of moves, Alice gets extra move => she can force inequality
        if total_q & 1:
            return True

        # Let D = lsum - rsum. Let x = (rq - lq)//2 * 9.
        D = lsum - rsum
        x = (rq - lq) // 2 * 9
        # If D equals x, Bob can balance; otherwise Alice wins
        return D != x
