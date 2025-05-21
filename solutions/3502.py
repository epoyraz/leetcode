class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        total_bad = 0
        base = ord('a')
        
        # For each start i, find the longest prefix length l_i
        # so that no character in s[i:i+l_i] reaches k occurrences.
        # Then all substrings of length 1..l_i starting at i are "bad"
        # (i.e. have max freq < k).
        for i in range(n):
            cnt = [0]*26
            # default: if we never hit k, we can go all the way to the end
            l_i = n - i
            for j in range(i, n):
                idx = ord(s[j]) - base
                cnt[idx] += 1
                if cnt[idx] == k:
                    # the substring s[i:j+1] just became "good",
                    # so the longest all-"bad" prefix ends at j-1
                    l_i = j - i
                    break
            total_bad += l_i

        # total substrings = n*(n+1)//2
        total_subs = n*(n+1)//2
        # answer = those with at least one char >= k = total_subs - total_bad
        return total_subs - total_bad
