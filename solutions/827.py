class Solution(object):
    def expressiveWords(self, s, words):
        def RLE(S):
            rle = []
            prev = S[0]
            count = 1
            for c in S[1:]:
                if c == prev:
                    count += 1
                else:
                    rle.append((prev, count))
                    prev = c
                    count = 1
            rle.append((prev, count))
            return rle
        
        s_rle = RLE(s)
        res = 0
        
        for word in words:
            w_rle = RLE(word)
            if len(w_rle) != len(s_rle):
                continue
            ok = True
            for (sc, scount), (wc, wcount) in zip(s_rle, w_rle):
                if sc != wc:
                    ok = False
                    break
                if scount < 3 and scount != wcount:
                    ok = False
                    break
                if scount >= 3 and wcount > scount:
                    ok = False
                    break
            if ok:
                res += 1
        return res
