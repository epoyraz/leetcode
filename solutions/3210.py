class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels_set = set('aeiou')
        count = 0
        n = len(s)

        for i in range(n):
            vowels = 0
            consonants = 0
            for j in range(i, n):
                if s[j] in vowels_set:
                    vowels += 1
                else:
                    consonants += 1
                if vowels == consonants and (vowels * consonants) % k == 0:
                    count += 1

        return count
