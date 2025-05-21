class Solution:
    def relocateMarbles(self, nums, moveFrom, moveTo):
        occupied = set(nums)

        for frm, to in zip(moveFrom, moveTo):
            if frm in occupied:
                occupied.remove(frm)
                occupied.add(to)

        return sorted(occupied)
