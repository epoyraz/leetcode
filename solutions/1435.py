class Solution:
    def xorQueries(self, arr, queries):
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)
        return [prefix[r + 1] ^ prefix[l] for l, r in queries]
