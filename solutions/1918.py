class Solution(object):
    def maximumScore(self, nums, k):
        n = len(nums)
        left = right = k
        min_val = nums[k]
        max_score = min_val

        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1
            min_val = min(min_val, nums[left], nums[right])
            max_score = max(max_score, min_val * (right - left + 1))

        return max_score
