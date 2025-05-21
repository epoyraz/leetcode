from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index, val):
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot):
        ans = 0
        for x in self.nums1:
            ans += self.freq2.get(tot - x, 0)
        return ans
