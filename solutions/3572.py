class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        # 1) Build needâcounts for word2 in a fixedâsize array of length 26
        freq_need = [0] * 26
        for c in word2:
            freq_need[ord(c) - 97] += 1
        # Count how many distinct letters actually must be met
        required = sum(1 for cnt in freq_need if cnt > 0)

        # 2) Sliding window over word1 with two pointers i (left) and r (right)
        freq_have = [0] * 26
        valid_met = 0   # how many of the required letters are currently satisfied
        r = 0
        ans = 0

        for i in range(n):
            # Expand r until we cover all required letters or hit the end
            while r < n and valid_met < required:
                idx = ord(word1[r]) - 97
                freq_have[idx] += 1
                if freq_need[idx] > 0 and freq_have[idx] == freq_need[idx]:
                    valid_met += 1
                r += 1

            # If we've satisfied all required counts, then every substring
            # starting at i with end â¥ r-1 is valid
            if valid_met == required:
                ans += (n - (r - 1))

            # Before moving iâi+1, remove word1[i] from the window
            idx = ord(word1[i]) - 97
            if freq_need[idx] > 0 and freq_have[idx] == freq_need[idx]:
                valid_met -= 1
            freq_have[idx] -= 1

        return ans
