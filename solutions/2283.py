class Solution:
    def sortEvenOdd(self, nums):
        even = sorted(nums[::2])             # sort even indices in non-decreasing order
        odd = sorted(nums[1::2], reverse=True)  # sort odd indices in non-increasing order

        result = []
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[e])
                e += 1
            else:
                result.append(odd[o])
                o += 1
        return result
