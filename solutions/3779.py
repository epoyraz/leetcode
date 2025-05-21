class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        n = len(pizzas)
        pizzas.sort()
        
        days = n // 4
        # Number of oddâday picks (Z on odd days)
        odd_cnt = (days + 1) // 2
        # Number of evenâday picks (Y on even days)
        even_cnt = days // 2
        
        # 1) Pick the oddâday gains: the largest `odd_cnt` pizzas
        total = sum(pizzas[n - odd_cnt:])
        
        # 2) From the remaining pizzas (all except those oddâday Zâs),
        #    we need for each even day one Y (the 2nd largest of a 4)
        #    and one Z â¥ Y (which will be âwastedâ).  To maximize the sum
        #    of the Yâs, we take the largest 2*even_cnt from what remains,
        #    pair them up in ascending order, and in each pair the smaller
        #    is our Y.
        rem = pizzas[:n - odd_cnt]
        # take the largest 2*even_cnt of rem
        S = rem[len(rem) - 2*even_cnt:]
        # sort is actually unnecessary since rem is sorted, and S is a suffix,
        # but we'll do it for clarity:
        S.sort()
        # sum every other starting at index 0 in that 2*even_cnt list
        total += sum(S[2*i] for i in range(even_cnt))
        
        return total
