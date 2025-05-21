class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def union(sets):
            res = set()
            for s in sets:
                res |= s
            return res

        def multi_product(sets):
            res = set([""])
            for s in sets:
                res = set(a + b for a in res for b in s)
            return res

        def parse(i):
            res = []
            curr = [set([""])]  # list of sets for concatenation
            while i < len(expression):
                if expression[i] == '{':
                    i, inner = parse(i + 1)
                    curr.append(inner)
                elif expression[i].isalpha():
                    curr.append(set([expression[i]]))
                    i += 1
                elif expression[i] == ',':
                    res.append(multi_product(curr))
                    curr = [set([""])]
                    i += 1
                elif expression[i] == '}':
                    res.append(multi_product(curr))
                    return i + 1, union(res)
            res.append(multi_product(curr))
            return i, union(res)

        _, result_set = parse(0)
        return sorted(result_set)
