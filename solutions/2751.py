class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        # freq of negatives from -50 to -1 mapped to 0..49
        freq = [0] * 50
        res = []
        neg_count = 0

        # Initialize first window
        for i in range(k):
            v = nums[i]
            if v < 0:
                idx = v + 50
                freq[idx] += 1
                neg_count += 1

        def get_xth():
            """Return x-th smallest negative or 0 if not enough"""
            if neg_count < x:
                return 0
            cnt = 0
            for idx in range(50):
                cnt += freq[idx]
                if cnt >= x:
                    return idx - 50
            return 0  # fallback

        # Record for the first window
        res.append(get_xth())

        # Slide window
        for i in range(k, n):
            # Remove nums[i-k]
            old = nums[i - k]
            if old < 0:
                oi = old + 50
                freq[oi] -= 1
                neg_count -= 1
            # Add nums[i]
            new = nums[i]
            if new < 0:
                ni = new + 50
                freq[ni] += 1
                neg_count += 1

            res.append(get_xth())

        return res
