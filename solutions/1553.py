class Solution(object):
    def countTriplets(self, arr):
        n = len(arr)
        px = [0] * (n + 1)
        for i in range(n):
            px[i+1] = px[i] ^ arr[i]
        ans = 0
        for i in range(n):
            for k in range(i+1, n):
                if px[i] == px[k+1]:
                    ans += k - i
        return ans
