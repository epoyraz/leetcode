class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {0: -1}
        max_len = 0
        mask = 0

        for i, ch in enumerate(s):
            digit = int(ch)
            mask ^= (1 << digit)

            if mask in seen:
                max_len = max(max_len, i - seen[mask])
            else:
                seen[mask] = i

            for j in range(10):
                test_mask = mask ^ (1 << j)
                if test_mask in seen:
                    max_len = max(max_len, i - seen[test_mask])

        return max_len
