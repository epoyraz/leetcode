class Solution:
    def beautySum(self, s):
        total = 0
        n = len(s)

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1

                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0)

                total += max_freq - min_freq

        return total
