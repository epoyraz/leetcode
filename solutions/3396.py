class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 1. Check minimum length
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False

        for ch in word:
            # 2. Allow only letters and digits
            if not (ch.isdigit() or ch.isalpha()):
                return False

            # 3. Track vowels and consonants
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        # 4. Must have at least one vowel and one consonant
        return has_vowel and has_consonant
