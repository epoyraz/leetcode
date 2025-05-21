class Solution:
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        prev = bottom - 1
        ans = 0
        for s in special:
            # floors between prev+1 and s-1 inclusive
            gap = s - prev - 1
            if gap > ans:
                ans = gap
            prev = s
        # after last special to top
        tail_gap = top - prev
        if tail_gap > ans:
            ans = tail_gap
        return ans
