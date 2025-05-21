import bisect

class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        n = len(s)
        la, lb = len(a), len(b)

        # 1) Gather all startâindices of substrings == a and == b
        startsA = []
        for i in range(n - la + 1):
            if s[i:i+la] == a:
                startsA.append(i)
        
        startsB = []
        for j in range(n - lb + 1):
            if s[j:j+lb] == b:
                startsB.append(j)
        
        # 2) Sort Bâstarts so we can binaryâsearch
        startsB.sort()

        res = []
        # 3) For each i in A, check if there is some j in B with |j-i| <= k
        for i in startsA:
            # find the first j >= i-k
            lo = bisect.bisect_left(startsB, i - k)
            # check if that j is <= i + k
            if lo < len(startsB) and startsB[lo] <= i + k:
                res.append(i)

        return res
