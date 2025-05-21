class Solution:
    def maxScoreIndices(self, nums):
        total_ones = sum(nums)
        max_score = total_ones  # i = 0, numsleft = [], numsright = nums
        zeros_left = 0
        result = [0]

        for i, num in enumerate(nums):
            if num == 0:
                zeros_left += 1
            else:
                total_ones -= 1
            score = zeros_left + total_ones
            if score > max_score:
                max_score = score
                result = [i + 1]
            elif score == max_score:
                result.append(i + 1)
        return result
