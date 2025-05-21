class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        best = 0
        
        # for each character c, find runs of c in s
        for c in set(s):
            # collect lengths of consecutive runs of c
            runs = []
            length = 0
            for ch in s:
                if ch == c:
                    length += 1
                else:
                    if length > 0:
                        runs.append(length)
                        length = 0
            if length > 0:
                runs.append(length)
            
            if sum(runs) < 3:
                # fewer than 3 occurrences total â cannot get 3 substrings of c^1
                continue
            
            max_run = max(runs)
            # try k from max_run down to 1
            for k in range(max_run, 0, -1):
                # total occurrences of substring c^k is sum over runs of max(L - k + 1, 0)
                occ = 0
                for L in runs:
                    if L >= k:
                        occ += (L - k + 1)
                        if occ >= 3:
                            break
                if occ >= 3:
                    best = max(best, k)
                    break  # no need to try smaller k for this character
        
        return best if best > 0 else -1
