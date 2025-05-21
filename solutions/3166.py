from collections import Counter
import math

class Solution:
    def minGroupsForValidAssignment(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # frequency of each distinct value
        cnt = Counter(nums).values()
        min_cnt = min(cnt)                # smallest frequency among all values
        ans = float("inf")

        # Let g be the minimum size of any box (1 â¦ min_cnt).
        # Every box then has size g or g+1.
        # For a count c, the fewest boxes needed is ceil(c/(g+1)).
        # Try every g; the total work over all g is O(sum cnt) â¤ 1e5.
        for g in range(1, min_cnt + 1):
            total_boxes = 0
            ok = True
            for c in cnt:
                # number of boxes for this value
                boxes = (c + g) // (g + 1)    # == ceil(c/(g+1))
                # Each box must have at least g balls,
                # so we need boxes * g â¤ c.  If not, g is impossible.
                if boxes * g > c:
                    ok = False
                    break
                total_boxes += boxes
            if ok:
                ans = min(ans, total_boxes)

        return ans if ans != float("inf") else len(nums)
