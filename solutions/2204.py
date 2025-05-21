class Solution:
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Pair each number with its index
        paired = [(num, i) for i, num in enumerate(nums)]
        # Sort by num descending; tie-breaker idx ascending doesn't matter
        paired.sort(key=lambda x: x[0], reverse=True)
        # Take top k elements
        topk = paired[:k]
        # Sort those by original index to restore subsequence order
        topk.sort(key=lambda x: x[1])
        # Extract the numbers
        return [num for num, _ in topk]
