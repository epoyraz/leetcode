class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        secret_count = {}
        guess_count = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1

        for digit in guess_count:
            if digit in secret_count:
                cows += min(secret_count[digit], guess_count[digit])

        return str(bulls) + "A" + str(cows) + "B"
