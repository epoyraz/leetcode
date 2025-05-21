class Solution:
    def sortArray(self, nums):
        # In-place heapsort: O(n log n) time, O(1) extra space
        n = len(nums)

        def sift_down(start, end):
            root = start
            while True:
                child = 2 * root + 1  # left child
                if child >= end:
                    break
                # pick the larger of the two children
                if child + 1 < end and nums[child + 1] > nums[child]:
                    child += 1
                # if root is smaller than the larger child, swap
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break

        # build max-heap
        for start in range(n // 2 - 1, -1, -1):
            sift_down(start, n)

        # extract elements from heap one by one
        for end in range(n - 1, 0, -1):
            # move current max to the end
            nums[0], nums[end] = nums[end], nums[0]
            # restore heap property on the reduced heap
            sift_down(0, end)

        return nums
