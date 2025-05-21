class Solution:
    def minimumTotalCost(self, nums1, nums2):
        n = len(nums1)
        bad = []
        freq = {}
        for i in range(n):
            if nums1[i] == nums2[i]:
                bad.append(i)
                freq[nums1[i]] = freq.get(nums1[i], 0) + 1

        if not bad:
            return 0

        majority_val = max(freq, key=freq.get)
        majority_cnt = freq[majority_val]
        need = max(0, 2 * majority_cnt - len(bad))

        extra = []
        if need:
            for i in range(n):
                if nums1[i] != nums2[i] and nums1[i] != majority_val and nums2[i] != majority_val:
                    extra.append(i)
                    if len(extra) == need:
                        break
            if len(extra) < need:
                return -1

        return sum(bad) + sum(extra)
