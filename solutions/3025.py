class Solution(object):
    def minOperations(self, nums, target):
        # Count of coins 2^k in nums
        cnt = [0] * 31
        for x in nums:
            k = x.bit_length() - 1
            cnt[k] += 1

        ops = 0
        for i in range(31):
            if (target >> i) & 1:
                # we need one 2^i
                if cnt[i] > 0:
                    cnt[i] -= 1
                else:
                    # find next larger coin to split
                    j = i + 1
                    while j < 31 and cnt[j] == 0:
                        j += 1
                    if j == 31:
                        return -1
                    # split down from j to i
                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ops += 1
                        j -= 1
                    cnt[i] -= 1  # use the newly created 2^i
            # after satisfying bit i, merge surplus small coins upward
            if i < 30:
                cnt[i + 1] += cnt[i] // 2

        return ops
