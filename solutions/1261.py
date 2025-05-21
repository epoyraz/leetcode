from collections import Counter

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        total_count = Counter(text)
        groups = []
        i = 0
        n = len(text)

        # Collect groups of consecutive characters
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j

        res = 0
        for i in range(len(groups)):
            char, count = groups[i]
            # Case 1: Use one swap to extend current group if there are extra chars
            res = max(res, min(count + 1, total_count[char]))

            # Case 2: Merge two groups separated by one different character
            if i + 2 < len(groups) and groups[i + 1][1] == 1 and groups[i][0] == groups[i + 2][0]:
                merged = groups[i][1] + groups[i + 2][1]
                if total_count[char] > merged:
                    merged += 1
                res = max(res, merged)

        return res
