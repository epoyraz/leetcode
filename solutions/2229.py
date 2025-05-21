class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        prefix = [0] * (n + 1)
        pos = [f[0] for f in fruits]

        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]

        def range_sum(left, right):
            # Return total fruits from index `left` to `right` (inclusive)
            return prefix[right + 1] - prefix[left]

        max_fruits = 0

        # Two pointer window over sorted fruit positions
        i = 0
        for j in range(n):
            # shrink left bound `i` until window [i, j] fits in k steps
            while i <= j:
                left_pos = fruits[i][0]
                right_pos = fruits[j][0]

                # walking from startPos to left_pos, then to right_pos
                dist = min(
                    abs(startPos - left_pos) + (right_pos - left_pos),
                    abs(startPos - right_pos) + (right_pos - left_pos)
                )
                if dist <= k:
                    break
                i += 1

            if i <= j:
                max_fruits = max(max_fruits, range_sum(i, j))

        return max_fruits
