class Solution:
    def countVowelSubstrings(self, word):
        """
        :param word: str
        :return: int  # number of vowel-only substrings containing all 5 vowels
        """
        vowels = set('aeiou')
        n = len(word)
        count = 0

        # Try every start index
        for i in range(n):
            seen = set()
            # Extend the substring from i to j
            for j in range(i, n):
                c = word[j]
                # If we hit a consonant, no longer a vowel-only substring
                if c not in vowels:
                    break
                seen.add(c)
                # Once we've seen all 5 vowels, every further extension
                # (still vowel-only) counts as another valid substring
                if len(seen) == 5:
                    count += 1

        return count
