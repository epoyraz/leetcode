class Solution(object):
    def minimalKSum(self, nums, k):
        nums = sorted(set(nums))
        ans = 0
        cur = 1

        for x in nums:
            if cur >= x:           # current already inside or past this number
                cur = x + 1
                continue

            gap = x - cur          # how many missing before x
            take = min(gap, k)     # how many of them we still need

            last = cur + take - 1
            ans += (cur + last) * take // 2  # sum of arithmetic sequence
            k -= take
            if k == 0:
                return ans

            cur = x + 1            # move just after x

        # still need k numbers after largest x
        last = cur + k - 1
        ans += (cur + last) * k // 2
        return ans
