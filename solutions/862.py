class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        changes = sorted(zip(indices, sources, targets), reverse=True)
        for idx, src, tgt in changes:
            if s[idx:idx+len(src)] == src:
                s = s[:idx] + tgt + s[idx+len(src):]
        return s
