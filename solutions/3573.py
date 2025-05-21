class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        # 1) build freq_need from word2
        freq_need = [0]*26
        for c in word2:
            freq_need[ord(c)-97] += 1
        # how many distinct letters we actually need to satisfy
        required = sum(1 for x in freq_need if x>0)

        # 2) sliding window [i..r-1], maintain freq_have + valid_count
        freq_have = [0]*26
        valid_count = 0   # how many characters c satisfy freq_have[c]>=freq_need[c]
        r = 0
        ans = 0

        for i in range(n):
            # 3) expand r until window covers word2 (or until end)
            while r < n and valid_count < required:
                idx = ord(word1[r]) - 97
                freq_have[idx] += 1
                # if this char is one we care about, and we just hit the needed count
                if freq_need[idx] > 0 and freq_have[idx] == freq_need[idx]:
                    valid_count += 1
                r += 1

            # now either valid_count==required (window [i..r-1] works)
            # or r==n and still invalid
            if valid_count == required:
                # any extension of [i..r-1] up to [i..n-1] remains valid
                ans += n - (r-1)

            # 4) before moving iâi+1, remove word1[i] from window
            idx = ord(word1[i]) - 97
            # if this char was just satisfying its need, removing it breaks validity
            if freq_need[idx] > 0 and freq_have[idx] == freq_need[idx]:
                valid_count -= 1
            freq_have[idx] -= 1

        return ans
