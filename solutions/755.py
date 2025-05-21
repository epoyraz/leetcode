class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        move, total = 0, 0
        while total < target or (total - target) % 2 != 0:
            move += 1
            total += move
        return move
