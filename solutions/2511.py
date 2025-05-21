class Solution:
    def minimumPartition(self, s, k):
        count = 1
        curr = 0
        for ch in s:
            curr = curr * 10 + (ord(ch) - ord('0'))
            if curr > k:
                # start a new substring at ch
                count += 1
                curr = ord(ch) - ord('0')
                if curr > k:
                    return -1
        return count
