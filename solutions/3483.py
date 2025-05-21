class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        # build diff array: 1 if adjacent differ, else 0
        diff = [0]*n
        for i in xrange(n):
            if colors[i] != colors[(i+1) % n]:
                diff[i] = 1
        
        # we need k-1 consecutive ones in diff, circularly.
        L = k - 1
        # extend diff by first L-1 elements to handle wrap
        ext = diff + diff[:L-1]
        
        # prefix sums
        ps = [0] * (len(ext)+1)
        for i in xrange(len(ext)):
            ps[i+1] = ps[i] + ext[i]
        
        # count windows of length L summing to L
        cnt = 0
        for start in xrange(n):
            if ps[start+L] - ps[start] == L:
                cnt += 1
        
        return cnt
