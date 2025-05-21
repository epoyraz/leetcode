class Solution(object):
    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        if k == 0:
            return True

        # 1) Record first and last positions of every char
        first = {c: n for c in "abcdefghijklmnopqrstuvwxyz"}
        last  = {c:-1 for c in "abcdefghijklmnopqrstuvwxyz"}
        for i, ch in enumerate(s):
            first[ch] = min(first[ch], i)
            last[ch]  = max(last[ch], i)

        # 2) Build the true minimal special substrings
        intervals = []
        for c in first:
            i = first[c]
            if i == n:
                # char c not present
                continue

            # expand to cover all last[...] in [i..end]
            end = last[c]
            j = i
            while j <= end:
                end = max(end, last[s[j]])
                j += 1

            # skip the entire string
            if i == 0 and end == n - 1:
                continue

            # verify that no char inside has a first-occurrence before i
            valid = True
            for x in s[i:end+1]:
                if first[x] < i:
                    valid = False
                    break
            if valid:
                intervals.append((i, end))

        # 3) Greedily pick as many non-overlapping as possible
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for start, finish in intervals:
            if start > last_end:
                count += 1
                last_end = finish
                if count >= k:
                    return True

        return False
