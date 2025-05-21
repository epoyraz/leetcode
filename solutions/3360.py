class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        import bisect
        
        # 1) Count frequencies of each letter
        cnt = Counter(word)
        F = sorted(cnt.values())  # list of positive frequencies
        m = len(F)
        
        # 2) Build prefix sums for fast rangeâsum queries
        P = [0]*(m+1)
        for i in range(m):
            P[i+1] = P[i] + F[i]
        
        total_sum = P[m]
        best = total_sum  # upper bound: delete everything
        
        # 3) Candidate L values: 0 and each unique frequency
        candidates_L = {0}
        candidates_L.update(F)
        
        for L in candidates_L:
            R = L + k
            # sum of deletions for f < L  => delete all of those letters
            idx_l = bisect.bisect_left(F, L)
            del_low = P[idx_l]
            
            # sum of deletions for f > R => delete excess above R
            idx_r = bisect.bisect_right(F, R)
            # sum of f_i for i in [idx_r..m-1] is (P[m]-P[idx_r])
            count_high = m - idx_r
            sum_high = P[m] - P[idx_r]
            del_high = sum_high - count_high * R
            
            cost = del_low + del_high
            if cost < best:
                best = cost
        
        return best
