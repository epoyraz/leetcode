class Solution(object):
    def minOperations(self, nums1, nums2):
        n = len(nums1)
        best = float('inf')

        # Try both possibilities for the last index: no swap (0) or swap (1)
        for swap_last in (0, 1):
            if swap_last == 0:
                a = nums1[-1]
                b = nums2[-1]
                cost = 0
            else:
                a = nums2[-1]
                b = nums1[-1]
                cost = 1

            valid = True
            # For each other index, determine if we must swap or not
            for i in range(n - 1):
                u, v = nums1[i], nums2[i]
                ok0 = (u <= a and v <= b)   # leave as is
                ok1 = (v <= a and u <= b)   # swap at i
                if not ok0 and not ok1:
                    valid = False
                    break
                if not ok0 and ok1:
                    cost += 1
                # if ok0 is True (regardless of ok1), pick no swap to minimize cost

            if valid:
                best = min(best, cost)

        return best if best != float('inf') else -1
