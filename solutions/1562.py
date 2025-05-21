class Solution:
    def peopleIndexes(self, favoriteCompanies):
        n = len(favoriteCompanies)
        sets = [set(lst) for lst in favoriteCompanies]
        res = []
        for i, s_i in enumerate(sets):
            is_subset = False
            for j, s_j in enumerate(sets):
                if i == j or len(s_i) > len(s_j):
                    continue
                if s_i.issubset(s_j):
                    is_subset = True
                    break
            if not is_subset:
                res.append(i)
        return res
