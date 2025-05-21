class Solution(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        
        # Precompute, for every pair of distinct rows (r1<r2),
        # an array best12[c]: the best sum of placing rooks in r1 and r2
        # on two distinct columns != c.
        best12 = {}
        for r1 in range(m):
            for r2 in range(r1+1, m):
                # Extract top-3 entries (value, col) from each row
                A = sorted(((board[r1][c], c) for c in range(n)),
                           reverse=True)[:3]
                B = sorted(((board[r2][c], c) for c in range(n)),
                           reverse=True)[:3]
                
                arr = [0]*n
                for forbid in range(n):
                    # build the filtered top-2 lists excluding 'forbid'
                    A2 = [(v,c) for v,c in A if c != forbid]
                    B2 = [(v,c) for v,c in B if c != forbid]
                    # must have at least two columns available overall
                    # and each list has length â¥ 2 since n â¥ 3
                    va1, i1 = A2[0]
                    vb1, j1 = B2[0]
                    if i1 != j1:
                        arr[forbid] = va1 + vb1
                    else:
                        va2, i2 = A2[1]
                        vb2, j2 = B2[1]
                        arr[forbid] = max(va1 + vb2, va2 + vb1)
                best12[(r1,r2)] = arr
        
        answer = -10**30
        # Now pick any 3 distinct rows r1<r2<r3.
        # For each column c3 assigned to r3, we can add best12[(r1,r2)][c3].
        for r1 in range(m):
            for r2 in range(r1+1, m):
                arr12 = best12[(r1,r2)]
                for r3 in range(r2+1, m):
                    # scan every possible column c3
                    row3 = board[r3]
                    best = -10**30
                    for c3 in range(n):
                        s = arr12[c3] + row3[c3]
                        if s > best:
                            best = s
                    if best > answer:
                        answer = best
        
        return answer
