class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        # Let x be jumbo, y be small
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices

        # From above: x = tomatoSlices/2 - cheeseSlices
        #             y = 2*cheeseSlices - tomatoSlices/2

        if tomatoSlices % 2 != 0:
            return []

        x = tomatoSlices // 2 - cheeseSlices
        y = cheeseSlices - x

        if x < 0 or y < 0:
            return []

        return [x, y]
