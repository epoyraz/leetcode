class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            new_s = []
            # split into groups of size k
            for i in range(0, len(s), k):
                group = s[i:i+k]
                # sum the digits in this group
                total = sum(ord(c) - ord('0') for c in group)
                new_s.append(str(total))
            s = "".join(new_s)
        return s
