class Solution:
    def arrayRankTransform(self, arr):
        # Create a sorted list of the unique values
        unique_sorted = sorted(set(arr))
        # Map each value to its rank (1-based index in the sorted unique list)
        rank = {v: i + 1 for i, v in enumerate(unique_sorted)}
        # Replace each element in arr with its rank
        return [rank[v] for v in arr]
