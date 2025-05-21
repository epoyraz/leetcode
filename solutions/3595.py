from collections import Counter

class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        B = n // k
        
        # Split s and t into k chunks of length B
        S_chunks = [s[i*B:(i+1)*B] for i in range(k)]
        T_chunks = [t[i*B:(i+1)*B] for i in range(k)]
        
        # If the multisets of chunks match, return True
        return Counter(S_chunks) == Counter(T_chunks)
