from collections import deque

class Solution(object):
    def kSimilarity(self, s1, s2):
        queue = deque()
        queue.append((s1, 0))
        visited = set()
        visited.add(s1)
        
        while queue:
            s, step = queue.popleft()
            if s == s2:
                return step
            i = 0
            while s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    lst = list(s)
                    lst[i], lst[j] = lst[j], lst[i]
                    ns = ''.join(lst)
                    if ns not in visited:
                        visited.add(ns)
                        queue.append((ns, step + 1))
