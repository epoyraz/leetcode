class Solution:
    def sortPeople(self, names, heights):
        # Pair each name with its height, sort by height descending
        paired = sorted(zip(heights, names), reverse=True)
        # Extract the names in sorted order
        return [name for _, name in paired]
