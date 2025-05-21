from collections import Counter

class Solution:
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Count how many times each string appears
        cnt = Counter(arr)
        
        # Iterate in original order, picking those with count==1
        distinct_seen = 0
        for s in arr:
            if cnt[s] == 1:
                distinct_seen += 1
                if distinct_seen == k:
                    return s
        
        # If fewer than k distinct strings, return empty
        return ""
