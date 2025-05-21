class Solution(object):
    def minimumRecolors(self, blocks, k):
        min_ops = float('inf')
        count_w = 0

        for i in range(k):
            if blocks[i] == 'W':
                count_w += 1
        min_ops = count_w

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count_w -= 1
            if blocks[i] == 'W':
                count_w += 1
            min_ops = min(min_ops, count_w)

        return min_ops
