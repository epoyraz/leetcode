class Solution(object):
    def longestCommonSubpath(self, n, paths):
        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE1 = 9113823
        BASE2 = 9726637

        def get_hashes(path, L):
            h1 = h2 = 0
            p1 = pow(BASE1, L, MOD1)
            p2 = pow(BASE2, L, MOD2)
            s = set()
            for i, v in enumerate(path):
                h1 = (h1 * BASE1 + v) % MOD1
                h2 = (h2 * BASE2 + v) % MOD2
                if i >= L:
                    h1 = (h1 - path[i - L] * p1) % MOD1
                    h2 = (h2 - path[i - L] * p2) % MOD2
                if i >= L - 1:
                    s.add((h1, h2))
            return s

        def check(L):
            common = get_hashes(paths[0], L)
            if not common:
                return False
            for p in paths[1:]:
                common &= get_hashes(p, L)
                if not common:
                    return False
            return True

        lo, hi, ans = 1, min(len(p) for p in paths), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
