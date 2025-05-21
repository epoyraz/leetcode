class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        # Track for each letter: last lowercase index, first uppercase index
        last_lower = [-1] * 26
        first_upper = [n] * 26
        has_lower = [False] * 26
        has_upper = [False] * 26
        for i, ch in enumerate(word):
            if 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')
                has_lower[idx] = True
                last_lower[idx] = i
            elif 'A' <= ch <= 'Z':
                idx = ord(ch) - ord('A')
                has_upper[idx] = True
                # record only first uppercase index
                if first_upper[idx] == n:
                    first_upper[idx] = i
        # Count special letters: appear both, and all lowers before first upper
        count = 0
        for idx in range(26):
            if has_lower[idx] and has_upper[idx] and last_lower[idx] < first_upper[idx]:
                count += 1
        return count