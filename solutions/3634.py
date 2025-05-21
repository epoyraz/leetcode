class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Precompute mirror for each lowercase letter
        # mirror['a'] = 'z', mirror['b'] = 'y', ..., mirror['z'] = 'a'
        mirror = { 
            chr(ord('a') + i): chr(ord('a') + 25 - i)
            for i in range(26)
        }
        
        # stacks[ch] will hold the indices of unpaired occurrences of ch
        stacks = { chr(ord('a')+i): [] for i in range(26) }
        
        score = 0
        
        for i, c in enumerate(s):
            m = mirror[c]
            if stacks[m]:
                # found a closest unmarked j < i with s[j] == m
                j = stacks[m].pop()
                score += i - j
                # both i and j are now marked, so we do NOT push i anywhere
            else:
                # no available mirror to pair withâkeep this occurrence for future
                stacks[c].append(i)
        
        return score
