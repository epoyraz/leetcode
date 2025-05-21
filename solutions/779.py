class Solution(object):
    def maxChunksToSorted(self, arr):
        sorted_arr = sorted(arr)
        count = res = 0
        freq = {}
        for a, b in zip(arr, sorted_arr):
            freq[a] = freq.get(a, 0) + 1
            if freq[a] == 0:
                del freq[a]
            freq[b] = freq.get(b, 0) - 1
            if freq[b] == 0:
                del freq[b]
            if not freq:
                res += 1
        return res
