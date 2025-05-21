class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Gather lengths of consecutive runs for each character
        runs = {}
        i = 0
        while i < n:
            ch = s[i]
            j = i + 1
            while j < n and s[j] == ch:
                j += 1
            length = j - i
            runs.setdefault(ch, []).append(length)
            i = j
        
        best = 0
        
        # For each character, binary-search the maximum k with at least 3 occurrences of c^k
        for ch, lengths in runs.items():
            total = sum(lengths)
            if total < 3:
                continue  # can't get 3 substrings of even length 1
            
            lo, hi = 1, max(lengths)
            # f(k) = total number of substrings equal to c^k
            #       = sum_{L in lengths} max(0, L - k + 1)
            def count_k(k):
                cnt = 0
                for L in lengths:
                    if L >= k:
                        cnt += L - k + 1
                        if cnt >= 3:
                            break
                return cnt
            
            # Find largest k such that count_k(k) >= 3
            while lo <= hi:
                mid = (lo + hi) // 2
                if count_k(mid) >= 3:
                    best = max(best, mid)
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return best if best > 0 else -1
