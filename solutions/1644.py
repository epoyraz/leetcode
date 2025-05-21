class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        # Step 1: record first and last index of each char
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)

        intervals = []

        # Step 2: Expand each character's range to include all its dependent characters
        for i in range(26):
            if first[i] > last[i]:
                continue
            l, r = first[i], last[i]
            j = l
            valid = True
            while j <= r:
                ch_idx = ord(s[j]) - ord('a')
                if first[ch_idx] < l:
                    l = first[ch_idx]
                    j = l  # restart
                if last[ch_idx] > r:
                    r = last[ch_idx]
                j += 1
            # After expansion, re-check
            j = l
            while j <= r:
                ch_idx = ord(s[j]) - ord('a')
                if first[ch_idx] < l or last[ch_idx] > r:
                    valid = False
                    break
                j += 1
            if valid:
                intervals.append((l, r))

        # Step 3: Greedily choose non-overlapping intervals with min total length
        intervals.sort(key=lambda x: x[1])  # sort by end
        res = []
        end = -1
        for l, r in intervals:
            if l > end:
                res.append(s[l:r+1])
                end = r

        return res
