class Solution:
    def findLatestStep(self, arr, m):
        n = len(arr)
        length = [0] * (n + 2)
        count = [0] * (n + 1)
        res = -1

        for step, x in enumerate(arr, 1):
            left = length[x - 1]
            right = length[x + 1]
            new_len = left + 1 + right

            # decrement counts of the old segments
            if left > 0:
                count[left] -= 1
            if right > 0:
                count[right] -= 1

            # update the segment length at the boundaries
            length[x - left] = new_len
            length[x + right] = new_len

            # increment count for the new segment
            count[new_len] += 1

            # if there's any segment of length m, record this step
            if count[m] > 0:
                res = step

        return res
