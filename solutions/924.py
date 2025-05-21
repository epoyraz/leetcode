class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        delta = (sumA - sumB) // 2
        setB = set(bobSizes)
        for a in aliceSizes:
            if a - delta in setB:
                return [a, a - delta]
