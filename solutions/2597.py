class Solution:
    def cycleLengthQueries(self, n, queries):
        res = []
        for u, v in queries:
            du = u.bit_length() - 1
            dv = v.bit_length() - 1
            cnt_u = cnt_v = 0

            # bring u and v to same depth
            while du > dv:
                u //= 2
                du -= 1
                cnt_u += 1
            while dv > du:
                v //= 2
                dv -= 1
                cnt_v += 1

            # climb until they meet at LCA
            while u != v:
                u //= 2
                v //= 2
                cnt_u += 1
                cnt_v += 1

            # cycle length = path_u + path_v + the added edge
            res.append(cnt_u + cnt_v + 1)
        return res
