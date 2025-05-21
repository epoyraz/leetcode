import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        # Doublyâlinkedâlist pointers
        left  = [i-1 for i in range(n)]
        right = [i+1 for i in range(n)]
        right[n-1] = -1

        alive = [True]*n
        vals  = nums[:]

        # Count initial inversions: positions i where vals[i] < vals[i-1]
        inv_count = 0
        for i in range(1, n):
            if vals[i] < vals[i-1]:
                inv_count += 1
        if inv_count == 0:
            return 0

        # Minâheap of (sum, left_index)
        heap = [(vals[i] + vals[i+1], i) for i in range(n-1)]
        heapq.heapify(heap)

        ops = 0
        while inv_count > 0 and heap:
            s, i = heapq.heappop(heap)
            j = right[i]
            # stale?
            if j == -1 or not alive[i] or not alive[j] or s != vals[i] + vals[j]:
                continue

            # Before removal: remove any inversions involving j or its neighbors
            #  â the pairs (j, left[j]) and (right[j], j)
            if left[j] != -1 and vals[j] < vals[left[j]]:
                inv_count -= 1
            if right[j] != -1 and vals[right[j]] < vals[j]:
                inv_count -= 1

            # Also remove the inversion at (i, left[i]) if it exists,
            # because vals[i] is about to change
            if left[i] != -1 and vals[i] < vals[left[i]]:
                inv_count -= 1

            # Merge j into i
            vals[i] = s
            alive[j] = False

            # Relink: skip over j
            r = right[j]
            right[i] = r
            if r != -1:
                left[r] = i

            # Push the two new adjacent sums involving i
            if left[i] != -1:
                heapq.heappush(heap, (vals[left[i]] + vals[i], left[i]))
            if r != -1:
                heapq.heappush(heap, (vals[i] + vals[r], i))

            # After merge: recheck the two adjacencies that may now be inverted
            #  â at (i, left[i]) and at (r, i)
            if left[i] != -1 and vals[i] < vals[left[i]]:
                inv_count += 1
            if r     != -1 and vals[r] < vals[i]:
                inv_count += 1

            ops += 1

        return ops
