class Solution:
    def maximumRemovals(self, s, p, removable):
        def is_subsequence(removed):
            i = j = 0
            while i < len(s) and j < len(p):
                if i in removed:
                    i += 1
                    continue
                if s[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)

        left, right = 0, len(removable)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            removed = set(removable[:mid])
            if is_subsequence(removed):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
