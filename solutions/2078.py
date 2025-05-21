class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        m = len(students)
        # Precompute compatibility scores
        compat = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                # count matching answers
                cnt = 0
                for a,b in zip(students[i], mentors[j]):
                    if a == b:
                        cnt += 1
                compat[i][j] = cnt

        # dp[mask]: max sum pairing first popcount(mask) students
        # with the set of mentors indicated by bits in mask
        N = 1 << m
        dp = [0]*N
        for mask in range(1, N):
            i = bin(mask).count("1") - 1  # student index to assign
            best = 0
            # try pairing student i with each mentor j in mask
            sub = mask
            while sub:
                j = (sub & -sub).bit_length() - 1
                prev = dp[mask ^ (1<<j)] + compat[i][j]
                if prev > best:
                    best = prev
                sub ^= (1<<j)
            dp[mask] = best

        return dp[N-1]
