class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        dug = set(map(tuple, dig))
        ans = 0
        for r1, c1, r2, c2 in artifacts:
            ok = True
            for r in xrange(r1, r2 + 1):
                for c in xrange(c1, c2 + 1):
                    if (r, c) not in dug:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                ans += 1
        return ans
