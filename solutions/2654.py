class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels = set('aeiou')
        count = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                count += 1
        return count
