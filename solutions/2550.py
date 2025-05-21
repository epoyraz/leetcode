class Solution:
    def twoEditWords(self, queries, dictionary):
        res = []
        for q in queries:
            for d in dictionary:
                # Count letter differences up to 3
                diff = 0
                for qc, dc in zip(q, d):
                    if qc != dc:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    res.append(q)
                    break
        return res
