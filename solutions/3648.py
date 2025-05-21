class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        n = len(fruits)
        NEG = -10**18

        # 1) Green child collects the main diagonal:
        diag_sum = 0
        for i in range(n):
            diag_sum += fruits[i][i]
            fruits[i][i] = 0  # zero it so red/blue won't double-count

        # 2) Red child DP (from (0,n-1) down to (n-1,n-1)):
        #    moves are (i,j) â (i+1, j-1),(i+1, j),(i+1, j+1)
        dp2 = [NEG] * n
        dp2[n-1] = fruits[0][n-1]
        for i in range(1, n):
            new = [NEG] * n
            for j in range(n):
                best_prev = dp2[j]
                if j > 0:      best_prev = max(best_prev, dp2[j-1])
                if j + 1 < n:  best_prev = max(best_prev, dp2[j+1])
                new[j] = best_prev + fruits[i][j]
            dp2 = new
        red_score = dp2[n-1]

        # 3) Blue child DP (from (n-1,0) to (n-1,n-1)):
        #    moves are (i,j) â (i-1, j+1),(i, j+1),(i+1, j+1)
        dp3 = [NEG] * n
        dp3[n-1] = fruits[n-1][0]  # <-- FIXED: start at row n-1, col 0
        for j in range(1, n):
            new = [NEG] * n
            for i in range(n):
                best_prev = dp3[i]
                if i > 0:      best_prev = max(best_prev, dp3[i-1])
                if i + 1 < n:  best_prev = max(best_prev, dp3[i+1])
                new[i] = best_prev + fruits[i][j]
            dp3 = new
        blue_score = dp3[n-1]

        return diag_sum + red_score + blue_score
