from collections import Counter

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def countPairs(self, nums, k):
        count = Counter()
        res = 0

        for num in nums:
            g = gcd(num, k)
            for x in count:
                if (g * x) % k == 0:
                    res += count[x]
            count[g] += 1

        return res
