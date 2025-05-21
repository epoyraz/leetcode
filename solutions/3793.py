class Solution(object):
    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        best = 1  # at least one character
        
        # Enumerate all substrings s[i:j] and t[u:v]
        # i in [0..n], j in [i..n]; u in [0..m], v in [u..m]
        for i in range(n + 1):
            for j in range(i, n + 1):
                len_s = j - i
                for u in range(m + 1):
                    for v in range(u, m + 1):
                        L = len_s + (v - u)
                        # Skip shorter concatenations
                        if L <= best:
                            continue
                        # Check palindrome on the fly
                        left, right = 0, L - 1
                        ok = True
                        while left < right:
                            # get char at left
                            if left < len_s:
                                cl = s[i + left]
                            else:
                                cl = t[u + (left - len_s)]
                            # get char at right
                            if right < len_s:
                                cr = s[i + right]
                            else:
                                cr = t[u + (right - len_s)]
                            if cl != cr:
                                ok = False
                                break
                            left += 1
                            right -= 1
                        if ok:
                            best = L
        return best
