class Solution(object):
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        sorted_indices = sorted(range(len(nums2)), key=lambda i: nums2[i])
        result = [0] * len(nums1)
        low, high = 0, len(nums1) - 1

        for i in reversed(sorted_indices):
            if nums1[high] > nums2[i]:
                result[i] = nums1[high]
                high -= 1
            else:
                result[i] = nums1[low]
                low += 1

        return result
