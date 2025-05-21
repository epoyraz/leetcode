class Solution(object):
    def beautifulSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        # Build rolling hash (64-bit) so substring equality is O(1)
        B = 91138233
        mask = (1<<64) - 1
        H = [0]*(n+1)
        P = [1]*(n+1)
        for i in range(n):
            H[i+1] = ((H[i]*B) + (nums[i]+1)) & mask
            P[i+1] = (P[i]*B) & mask
        def get_hash(l, r):
            # hash of nums[l:r]
            return (H[r] - (H[l]*P[r-l] & mask)) & mask

        ans = 0
        # i splits nums1=[0..i-1], nums2=[i..j-1], nums3=[j..n-1]
        for i in range(1, n-1):
            # Precompute whether nums1 is a prefix of nums2:
            # requires length of nums2 >= length(nums1) i.e. j-i >= i â j>=2*i
            h_pref1 = get_hash(0, i)
            h_pref2 = get_hash(i, 2*i) if 2*i <= n else None
            cond1_base = (2*i <= n and h_pref1 == h_pref2)

            for j in range(i+1, n):
                L2 = j - i   # length of nums2
                # Condition A: nums1 is prefix of nums2
                ok = False
                if cond1_base and j >= 2*i:
                    ok = True
                else:
                    # Condition B: nums2 is prefix of nums3
                    # need nums3 length >= nums2 length â n-j >= L2 â j+L2<=n
                    if j + L2 <= n:
                        if get_hash(i, j) == get_hash(j, j+L2):
                            ok = True

                if ok:
                    ans += 1

        return ans
