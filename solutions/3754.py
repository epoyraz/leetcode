import heapq

class Solution(object):
    def maxDistance(self, s, k):
        # unit-step vectors
        dx = {'N':0, 'S':0, 'E':1, 'W':-1}
        dy = {'N':1, 'S':-1, 'E':0, 'W':0}

        max_global = 0

        # try all four sign-pairs (s_x, s_y)
        for sx, sy in ((1,1), (1,-1), (-1,1), (-1,-1)):
            # precompute each direction's signed weight, and the best possible step
            weight = {c: sx*dx[c] + sy*dy[c] for c in 'NSEW'}
            best_step = max(weight.values())

            signed_sum = 0   # running dot-product
            sum_sel    = 0   # sum of the top-k improvements so far
            selected   = []  # min-heap of selected r's
            eligible   = []  # max-heap (via negatives) of the rest

            best_this_pass = 0

            for c in s:
                w = weight[c]
                signed_sum += w

                # improvement if we changed this move to the best possible one
                r = best_step - w
                if r > 0:
                    heapq.heappush(eligible, -r)

                # if we still have room, pull the best from eligible
                while len(selected) < k and eligible:
                    rr = -heapq.heappop(eligible)
                    heapq.heappush(selected, rr)
                    sum_sel += rr

                # if there's a better candidate than our current worst in selected, swap
                if eligible and selected and -eligible[0] > selected[0]:
                    rr = -heapq.heappop(eligible)
                    rs = heapq.heapreplace(selected, rr)
                    sum_sel += rr - rs

                # current achievable dot = exact prefix + best k edits
                curr = signed_sum + sum_sel
                if curr > best_this_pass:
                    best_this_pass = curr

            # update across all sign-pairs
            if best_this_pass > max_global:
                max_global = best_this_pass

        return max_global
