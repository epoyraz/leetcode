from collections import Counter

class Solution:
    def findSmallestInteger(self, nums, value):
        # Count how many nums fall into each remainder class mod âvalueâ
        freq = Counter(x % value for x in nums)
        
        # Try mex = 0,1,2,â¦; for each i we need one element with remainder i%value
        mex = 0
        while True:
            r = mex % value
            if freq[r] > 0:
                # we âuse upâ one such element to cover this mex
                freq[r] -= 1
                mex += 1
            else:
                # no element left that can be moved to i, so mex stops here
                return mex
