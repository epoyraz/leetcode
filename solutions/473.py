class Solution:
    def makesquare(self, matchsticks):
        if not matchsticks:
            return False

        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return all(side == target for side in sides)
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False

        return dfs(0)
