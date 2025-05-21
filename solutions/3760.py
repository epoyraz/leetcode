class Solution(object):
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        if not groups or not elements:
            return [-1] * len(groups)

        m = len(elements)
        maxg = max(groups)
        # Use m as "infinity" sentinel since valid indices are 0..m-1
        INF = m

        # 1) For each element value e â¤ maxg, record the smallest index j where elements[j] == e
        minIdx = [INF] * (maxg + 1)
        for j, e in enumerate(elements):
            if e <= maxg and j < minIdx[e]:
                minIdx[e] = j

        # 2) Build ansArr[g] = minimum j such that e divides g, or INF if none
        ansArr = [INF] * (maxg + 1)
        for e in range(1, maxg + 1):
            idx = minIdx[e]
            if idx < INF:
                # e is present in elements; it divides all multiples of e
                for multiple in range(e, maxg + 1, e):
                    if idx < ansArr[multiple]:
                        ansArr[multiple] = idx

        # 3) Assign for each group
        result = []
        for g in groups:
            if ansArr[g] < INF:
                result.append(ansArr[g])
            else:
                result.append(-1)

        return result
