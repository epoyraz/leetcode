from collections import Counter

class Solution:
    def frequencySort(self, s):
        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda x: -x[1])
        return ''.join(char * freq for char, freq in sorted_chars)
