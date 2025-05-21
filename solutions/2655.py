class Solution(object):
    def maxScore(self, nums):
        nums.sort(reverse=True)
        score = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum > 0:
                score += 1
            else:
                break
        return score
