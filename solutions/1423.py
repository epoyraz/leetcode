from collections import Counter

class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        count = Counter()
        max_occurrences = 0

        for i in range(len(s) - minSize + 1):
            substr = s[i:i + minSize]
            unique_letters = len(set(substr))
            if unique_letters <= maxLetters:
                count[substr] += 1
                max_occurrences = max(max_occurrences, count[substr])

        return max_occurrences
