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
        n = len(word)
        vowels = set('aeiou')
        # Track last occurrence of each vowel
        last_occ = {v: -1 for v in vowels}
        # For consonant positions
        cons_indices = []
        # Last consonant index, for k==0 case
        last_cons = -1
        result = 0
        for j, c in enumerate(word):
            if c in vowels:
                last_occ[c] = j
            else:
                cons_indices.append(j)
                last_cons = j
            # If any vowel hasn't appeared, skip
            left_v = min(last_occ.values())
            if left_v < 0:
                continue
            # Handle k == 0 separately (no consonants)
            if k == 0:
                # Start must be after last consonant
                lb = last_cons + 1
                # And start must be <= leftmost vowel to include all vowels
                ub = left_v
                if ub >= lb:
                    result += (ub - lb + 1)
            else:
                t = len(cons_indices)
                if t < k:
                    continue
                # First consonant index to include in substring
                first_cons = cons_indices[t - k]
                # Lower bound: start must be after previous consonant
                if t - k - 1 >= 0:
                    lb = cons_indices[t - k - 1] + 1
                else:
                    lb = 0
                # Upper bound: start must be <= first_cons to include exactly k total consonants
                ub = first_cons
                # Also start <= left_v to include all vowels
                ub = min(ub, left_v)
                if ub >= lb:
                    result += (ub - lb + 1)
        return result