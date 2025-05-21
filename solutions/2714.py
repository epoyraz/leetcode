class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n

        # Build leftSum
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

        # Build rightSum
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        # Compute answer
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])

        return answer
