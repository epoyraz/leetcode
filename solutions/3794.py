class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n, m = len(skill), len(mana)
        # M[i] = the time at which wizard i finishes the last brewed potion
        M = [0]*n

        # iterate over potions 0..m-1 in order
        for j in range(m):
            # compute prefix sums of processing times for potion j
            # prefix[i] = sum of skill[0]*mana[j] + ... + skill[i-1]*mana[j]
            # prefix[0] = 0
            prefix = 0
            best_t = 0

            # First pass: find the earliest start t so that
            # for all i: t + prefix >= M[i]  â  t >= M[i] - prefix
            for i in range(n):
                # processing time of wizard i on potion j
                p = skill[i]*mana[j]
                # we compare M[i] - prefix
                diff = M[i] - prefix
                if diff > best_t:
                    best_t = diff
                # advance prefix by p for next i
                prefix += p

            # Now best_t is the start time on wizard 0.
            # Second pass: update M[i] = completion time on wizard i
            # which is best_t + sum of p[0..i]
            running = best_t
            for i in range(n):
                running += skill[i]*mana[j]
                M[i] = running

        # when the last wizard finishes the last potion:
        return M[-1]
