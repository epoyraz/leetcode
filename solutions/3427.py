class Solution:
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        # 1) mark âbadâ adjacent pairs (same parity)
        bad = [0] * n
        for i in range(1, n):
            if nums[i] % 2 == nums[i-1] % 2:
                bad[i] = 1

        # 2) build prefix sums over bad[]
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i-1] + bad[i]

        # 3) answer each query in O(1)
        ans = []
        for l, r in queries:
            if l == r:
                # single element is always âspecialâ
                ans.append(True)
            else:
                # if there are no bad marks between l+1 and r, itâs special
                ans.append(pref[r] - pref[l] == 0)
        return ans
