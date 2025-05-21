class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        n = len(nums)
        L = len(nums[0])
        
        # We'll build, for each trim t = 1..L, the list of indices
        # sorted by their rightmost t digits (lex order, tie-breaking by index).
        # We do an LSD radix build: start from trim=1, then extend to trim=2, etc.
        sorted_idx = list(range(n))
        sorted_by_trim = [None] * (L + 1)
        
        for t in range(1, L+1):
            # stable counting sort on the t-th digit from the right
            buckets = [[] for _ in range(10)]
            pos = L - t
            for i in sorted_idx:
                d = ord(nums[i][pos]) - ord('0')
                buckets[d].append(i)
            # flatten
            sorted_idx = []
            for bucket in buckets:
                sorted_idx.extend(bucket)
            sorted_by_trim[t] = sorted_idx[:]  # snapshot
        
        # answer each query in O(1)
        ans = []
        for k, trim in queries:
            ans.append(sorted_by_trim[trim][k-1])
        return ans
