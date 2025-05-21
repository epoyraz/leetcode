class Solution(object):
    def maxPalindromesAfterOperations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter

        # 1) Count total pairs available in the global pool of letters
        total_counts = Counter()
        for w in words:
            total_counts.update(w)
        total_pairs = sum(v // 2 for v in total_counts.values())

        # 2) For each word, compute how many pairs it needs to become a palindrome
        #    A palindrome of length L requires floor(L/2) matching pairs
        needed_pairs = [len(w) // 2 for w in words]

        # 3) Greedily take words needing the fewest pairs first
        needed_pairs.sort()
        used = 0
        count = 0
        for need in needed_pairs:
            if used + need <= total_pairs:
                used += need
                count += 1
            else:
                break

        return count
