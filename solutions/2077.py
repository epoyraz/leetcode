class Solution(object):
    def maximumNumber(self, num, change):
        s = list(num)
        n = len(s)
        i = 0
        # 1) Find start of mutation: first position where change[d] > original
        while i < n and change[ord(s[i]) - ord('0')] <= ord(s[i]) - ord('0'):
            i += 1
        # If no such position, no mutation helps
        if i == n:
            return num
        # 2) Mutate substring while it doesn't decrease digits
        while i < n and change[ord(s[i]) - ord('0')] >= ord(s[i]) - ord('0'):
            s[i] = str(change[ord(s[i]) - ord('0')])
            i += 1
        return "".join(s)
