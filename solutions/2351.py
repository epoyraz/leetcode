class Solution:
    def waysToBuyPensPencils(self, total, cost1, cost2):
        ways = 0
        # Try buying x pens for x = 0..max pens you can afford
        for x in range(total // cost1 + 1):
            remaining = total - cost1 * x
            # With the remaining money, you can buy 0..(remaining//cost2) pencils
            ways += remaining // cost2 + 1
        return ways
