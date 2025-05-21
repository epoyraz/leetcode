from collections import Counter

class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        freq = Counter()
        
        # For each day, count each response at most once
        for day in responses:
            for resp in set(day):
                freq[resp] += 1
        
        # Find the maximum frequency
        max_count = max(freq.values())
        
        # Among those with max_count, pick lexicographically smallest
        candidates = [resp for resp, cnt in freq.items() if cnt == max_count]
        return min(candidates)
