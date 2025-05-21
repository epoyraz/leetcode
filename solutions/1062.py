class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        count, curr_sum = 0, 0

        for num in arr:
            curr_sum += num
            if curr_sum == target:
                count += 1
                curr_sum = 0

        return count >= 3
