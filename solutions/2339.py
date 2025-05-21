class Solution:
    def countDistinct(self, nums, k, p):
        """
        Count distinct subarrays of nums with at most k elements divisible by p.
        """
        root = {}   # trie root
        ans = 0
        n = len(nums)
        
        for i in range(n):
            node = root
            cnt = 0
            for j in range(i, n):
                x = nums[j]
                if x % p == 0:
                    cnt += 1
                    if cnt > k:
                        break
                # Insert nums[j] into trie if not already present
                if x not in node:
                    node[x] = {}
                    ans += 1
                node = node[x]
        
        return ans
