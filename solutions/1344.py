from collections import Counter, defaultdict

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = defaultdict(int)
        res = 0
        maxFreq = 0

        for i, num in enumerate(nums):
            prev = count[num]
            if prev > 0:
                freq[prev] -= 1
            count[num] += 1
            curr = count[num]
            freq[curr] += 1
            maxFreq = max(maxFreq, curr)

            total = i + 1

            if (
                maxFreq == 1 or
                freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == total and freq[maxFreq] == 1 or
                freq[1] == 1 and freq[maxFreq] * maxFreq + 1 == total
            ):
                res = total

        return res
