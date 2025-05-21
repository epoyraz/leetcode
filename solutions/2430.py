class Solution:
    def countExcellentPairs(self, nums, k):
        # Only unique values matter
        nums = set(nums)
        
        # Count how many numbers have each popcount
        from collections import Counter
        cnt = Counter(bin(x).count("1") for x in nums)
        
        # Build a sorted list of (popcount, frequency)
        # but since popcounts range only up to ~30, we can use an array
        maxc = max(cnt) if cnt else 0
        freq = [0] * (maxc + 1)
        for c, f in cnt.items():
            freq[c] = f
        
        # Build suffix sums: suff[c] = sum_{j>=c} freq[j]
        n = len(freq)
        suff = [0] * (n + 2)
        for c in range(n - 1, -1, -1):
            suff[c] = suff[c+1] + freq[c]
        
        # For each popcount c1, we need popcount c2 >= k - c1
        ans = 0
        for c1, f1 in enumerate(freq):
            if f1 == 0:
                continue
            need = k - c1
            if need <= 0:
                # any c2 works
                ans += f1 * len(nums)
            elif need < len(suff):
                ans += f1 * suff[need]
            # else need > max popcount => no contribution
        
        return ans
