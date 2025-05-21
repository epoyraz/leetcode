class Solution(object):
    def canTransform(self, start, end):
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        n = len(start)
        i = j = 0
        
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i == n and j == n:
                return True
            if i == n or j == n:
                return False
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        
        return True
