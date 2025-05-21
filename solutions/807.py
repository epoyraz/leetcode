class Solution(object):
    def customSortString(self, order, s):
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        res = []
        for ch in order:
            if ch in count:
                res.append(ch * count[ch])
                del count[ch]
        
        for ch in count:
            res.append(ch * count[ch])
        
        return ''.join(res)
