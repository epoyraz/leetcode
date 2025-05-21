class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        A = sorted(nums1)
        B = sorted(nums2)
        m = len(A)
        n = len(B)  # = m - 2

        ans = float('inf')
        # Try removing A[i] and A[j]
        for i in range(m):
            for j in range(i+1, m):
                x = None
                valid = True
                # walk through A skipping i,j
                t = 0  # index in B
                for k in range(m):
                    if k == i or k == j:
                        continue
                    diff = B[t] - A[k]
                    if x is None:
                        x = diff
                    elif diff != x:
                        valid = False
                        break
                    t += 1
                if valid:
                    ans = min(ans, x)

        return ans
