class Solution:
    def maxDistance(self, nums1, nums2):
        i = j = ans = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans
