class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        # keys 2 to 9 â 8 keys
        # assign 1st 8 letters to push 1
        # next 8 to push 2, etc.
        pushes = 0
        for i in range(n):
            pushes += (i // 8) + 1
        return pushes
