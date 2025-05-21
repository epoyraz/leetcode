class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Split p = A * B
        star = p.index('*')
        A = p[:star]
        B = p[star+1:]
        n, m = len(s), len(B)
        
        # Specialâcases: if A and B are both empty then "*" matches the empty substring
        if not A and not B:
            return True
        
        # Gather all positions where B occurs in s
        # (if B is empty, every position i in [0..n] is a valid "end of suffix")
        posB = []
        if B:
            for j in range(n - len(B) + 1):
                if s[j:j+len(B)] == B:
                    posB.append(j)
        else:
            # Treat suffixâmatch (empty B) as valid at every j from 0..n
            posB = list(range(n+1))
        
        # Now look for A somewhere before one of those Bâmatches:
        #   find an index i where s[i:i+len(A)] == A
        #   and there exists j in posB with j >= i+len(A)
        if A:
            for i in range(n - len(A) + 1):
                if s[i:i+len(A)] == A:
                    # We need some j â¥ i + len(A)
                    # Since posB is small (â¤ 50), just linearâscan:
                    for j in posB:
                        if j >= i + len(A):
                            return True
            return False
        else:
            # A is empty, so we only need B to occur somewhere (we already found posB)
            return bool(posB)
