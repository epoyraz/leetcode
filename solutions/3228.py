class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        n = len(nums1)
        half = n // 2

        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2

        # max we can pick is half from each list
        # but we must avoid duplicate selections
        unique1 = len(set1)
        unique2 = len(set2)
        overlap = len(common)

        # pick at most half from each
        from1 = min(half, unique1)
        from2 = min(half, unique2)

        # if overlap is too big, set size gets reduced
        if from1 + from2 <= len(set1 | set2):
            return from1 + from2
        return len(set1 | set2)
