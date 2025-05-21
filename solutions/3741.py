import bisect

class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        # durations of each meeting
        d = [endTime[i] - startTime[i] for i in range(n)]
        # g[j] = free time before meeting j (for j=0),
        # between meeting j-1 and j (1 <= j <= n-1),
        # and after meeting n-1 (j = n)
        g = [0] * (n + 1)
        g[0] = startTime[0]
        for j in range(1, n):
            g[j] = startTime[j] - endTime[j - 1]
        g[n] = eventTime - endTime[n - 1]

        # Sort g for fast ">= d_i" counts
        sorted_g = sorted(g)
        L = n + 1

        # Original maximum free slot without any move
        original_max = sorted_g[-1]

        # Precompute global largest (M1), its count, and secondâlargest (M2)
        M1 = original_max
        count1 = sum(1 for x in g if x == M1)
        # find the next smaller value
        M2 = 0
        for x in reversed(sorted_g):
            if x < M1:
                M2 = x
                break

        ans = original_max

        for i in range(n):
            di = d[i]
            # free time if we remove meeting i (merging g[i] and g[i+1])
            fi = g[i] + di + g[i + 1]

            # how many original gâs are >= di?
            idx = bisect.bisect_left(sorted_g, di)
            number_ge = L - idx
            # subtract g[i], g[i+1] if they counted
            subtract = (1 if g[i] >= di else 0) + (1 if g[i + 1] >= di else 0)
            Ki = number_ge - subtract

            # compute max free among the other gâs after removing g[i],g[i+1]
            if count1 >= 2:
                g_excl = M1
            else:
                # only one occurrence of M1 in g
                if g[i] == M1 or g[i + 1] == M1:
                    g_excl = M2
                else:
                    g_excl = M1

            # if there's some other slot >= di, we can place meeting i there
            # and leave fi untouched as the largest free gap
            if Ki > 0:
                candidate = fi
            else:
                # otherwise we must place into the fi gap itself,
                # reducing it by di, so max free is max(g_excl, fi - di)
                candidate = max(g_excl, fi - di)

            ans = max(ans, candidate)

        return ans
