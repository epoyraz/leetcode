class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        possible = set()

        def dfs(i, total):
            if i == len(toppingCosts):
                possible.add(total)
                return
            for count in range(3):
                dfs(i + 1, total + count * toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)

        return min(possible, key=lambda x: (abs(x - target), x))
