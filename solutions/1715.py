class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.ans = 0
        n = len(s)
        
        def dfs(start, used, count):
            # Prune if even using minimal-length substrings (length=1),
            # we cannot exceed current best
            if count + (n - start) <= self.ans:
                return
            if start == n:
                self.ans = max(self.ans, count)
                return
            # Try all end positions for the next substring
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if sub not in used:
                    used.add(sub)
                    dfs(end, used, count + 1)
                    used.remove(sub)
        
        dfs(0, set(), 0)
        return self.ans
