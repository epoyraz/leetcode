class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        best = []
        # Try every index as the start of the subsequence
        for i in range(n):
            seq = [i]
            last = groups[i]
            for j in range(i+1, n):
                if groups[j] != last:
                    seq.append(j)
                    last = groups[j]
            if len(seq) > len(best):
                best = seq
        # Map indices back to words
        return [words[i] for i in best]
