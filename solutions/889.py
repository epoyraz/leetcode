class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        
        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
