class Solution(object):
    def minTimeToType(self, word):
        pos = ord('a')
        time = 0
        for ch in word:
            target = ord(ch)
            diff = abs(pos - target)
            time += min(diff, 26 - diff) + 1
            pos = target
        return time
