class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = 'a'
        while len(word) < k:
            shifted = ''.join(
                chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
                for c in word
            )
            word += shifted
        return word[k-1]

    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        result = 0
        # Iterate over all possible start indices
        for i in range(n):
            # Counts of each vowel in the current window
            vowel_count = {v: 0 for v in vowels}
            consonants = 0
            # Extend the substring from i to j
            for j in range(i, n):
                c = word[j]
                if c in vowels:
                    vowel_count[c] += 1
                else:
                    consonants += 1
                # If consonants exceed k, no further extension from this i will work
                if consonants > k:
                    break
                # Check if all vowels are present and consonant count matches k
                if consonants == k and all(vowel_count[v] > 0 for v in vowels):
                    result += 1
        return result