class Solution:
    def countVowels(self, word):
        """
        :param word: str
        :return: int  # sum of vowels over all substrings
        """
        n = len(word)
        vowels = set('aeiou')
        total = 0

        for i, ch in enumerate(word):
            if ch in vowels:
                # number of substrings including position i is (i+1)*(n-i)
                total += (i + 1) * (n - i)

        return total
