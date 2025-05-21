from collections import Counter

class Solution:
    def originalDigits(self, s):
        count = Counter(s)
        out = [0] * 10
        
        out[0] = count['z']
        out[2] = count['w']
        out[4] = count['u']
        out[6] = count['x']
        out[8] = count['g']
        
        out[3] = count['h'] - out[8]
        out[5] = count['f'] - out[4]
        out[7] = count['s'] - out[6]
        
        out[1] = count['o'] - out[0] - out[2] - out[4]
        out[9] = count['i'] - out[5] - out[6] - out[8]
        
        res = []
        for i in range(10):
            res.append(str(i) * out[i])
        
        return ''.join(res)
