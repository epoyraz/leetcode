class Solution:
    def unequalTriplets(self, nums):
        n = len(nums)
        from collections import Counter
        cnt = Counter(nums)
        
        # We'll count triples by fixing the middle element j
        # For each j, count number of i<j with nums[i]!=nums[j],
        # and number of k>j with nums[k]!=nums[j] and nums[k]!=nums[i].
        # A simpler formula: total pairs of distinct on left * total distinct on right,
        # minus pairs where left value == right value.
        
        # But an even simpler O(n + U^2) is:
        # Let pref and suff be frequency maps for left/right of j.
        pref = Counter()
        suff = cnt.copy()
        
        ans = 0
        # iterate j from 0 to n-1
        for j in range(n):
            x = nums[j]
            # remove current from right
            suff[x] -= 1
            if suff[x] == 0:
                del suff[x]
            
            # count of left positions is j, right is n-j-1
            # total ways to pick i in left â  x: j - pref[x]
            left_total = j - pref.get(x, 0)
            # total ways to pick k in right â  x: (n-j-1) - suff.get(x,0)
            right_total = (n - j - 1) - suff.get(x, 0)
            
            # but among those left i and right k, we must also ensure nums[i] != nums[k].
            # The total pairs left_total*right_total counts pairs where nums[i] == nums[k] too.
            # For each value v â  x, the bad pairs = pref[v] * suff[v].
            bad = 0
            for v in pref:
                if v == x:
                    continue
                bad += pref[v] * suff.get(v, 0)
            
            ans += left_total * right_total - bad
            
            # add current to left
            pref[x] += 1
        
        return ans
