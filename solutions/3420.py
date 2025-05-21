class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        # Record all the indices where nums[i] == x
        positions = []
        for i, num in enumerate(nums):
            if num == x:
                positions.append(i)
        
        # For each query, pick the (q-1)-th index if it exists
        answer = []
        count = len(positions)
        for q in queries:
            if q <= count:
                answer.append(positions[q-1])
            else:
                answer.append(-1)
        
        return answer