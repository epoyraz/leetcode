class Solution:
    def minimumBuckets(self, hamsters):
        n = len(hamsters)
        buckets = [False] * n
        ans = 0
        
        for i in range(n):
            if hamsters[i] == 'H':
                # already fed by a bucket on the left?
                if i > 0 and buckets[i-1]:
                    continue
                # try to place on the right
                if i+1 < n and hamsters[i+1] == '.' and not buckets[i+1]:
                    buckets[i+1] = True
                    ans += 1
                # otherwise, try to place on the left
                elif i > 0 and hamsters[i-1] == '.' and not buckets[i-1]:
                    buckets[i-1] = True
                    ans += 1
                else:
                    return -1
        
        return ans
