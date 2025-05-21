class Solution:
    def readBinaryWatch(self, turnedOn):
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(str(h) + ":" + ("%02d" % m))
        return res
