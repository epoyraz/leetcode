import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        n = len(intervals)
        if n == 0:
            return []

        # Augment intervals with original indices: (start, end, weight, original_index)
        s_intervals = []
        for i in range(n):
            s_intervals.append((intervals[i][0], intervals[i][1], intervals[i][2], i))

        # Sort intervals: primary key end point, secondary key start point, tertiary original index.
        s_intervals.sort(key=lambda x: (x[1], x[0], x[3]))

        # r_coords stores end points of s_intervals for efficient binary search.
        r_coords = [interval[1] for interval in s_intervals]

        # dp[k][i] stores (max_score, list_of_original_indices) for choosing k intervals,
        # with s_intervals[i] being the k-th interval.
        # max_so_far[k][i] stores the best (score, list_indices) for choosing k intervals
        # from s_intervals[0...i].
        # k ranges from 1 to 4. We use 0-indexed arrays of size 5 for k.
        dp = [[(-1, []) for _ in range(n)] for _ in range(5)]
        max_so_far = [[(-1, []) for _ in range(n)] for _ in range(5)]

        # Helper function to compare two (score, list_indices) tuples
        def best_of(val1, val2):
            s1, l1 = val1
            s2, l2 = val2

            if s1 == -1: return val2
            if s2 == -1: return val1
            
            if s1 > s2: return val1
            if s2 > s1: return val2
            
            if l1 < l2: return val1
            else: return val2

        # Dynamic Programming
        for k_count in range(1, 5): # k_count = number of intervals to choose (1 to 4)
            for i in range(n): # i = index in s_intervals
                l_i, r_i, w_i, original_idx_i = s_intervals[i]
                
                # Find best previous state for k_count-1 intervals
                # p is the largest index in s_intervals such that s_intervals[p].end < l_i AND p < i.
                # bisect_left on r_coords[0...i-1] finds insertion point for l_i.
                p_search_idx = bisect.bisect_left(r_coords, l_i, 0, i)
                p = p_search_idx - 1
                
                prev_choice_tuple = (-1, [])
                if k_count == 1:
                    # Base case for 1st interval: prev state is (score 0, empty list)
                    prev_choice_tuple = (0, [])
                elif p != -1: # If a valid predecessor region s_intervals[0...p] exists
                    # max_so_far[k_count-1][p] has the best choice for k_count-1 intervals ending by s_intervals[p]
                    prev_choice_tuple = max_so_far[k_count-1][p] 
                
                if prev_choice_tuple[0] != -1: # If a valid previous state chain exists
                    prev_score, prev_indices = prev_choice_tuple
                    current_score = w_i + prev_score
                    
                    current_indices_list = prev_indices + [original_idx_i]
                    current_indices_list.sort() # Keep sorted for lexicographical comparison

                    dp[k_count][i] = (current_score, current_indices_list)
                
                # Update max_so_far[k_count][i]
                if i == 0:
                    max_so_far[k_count][i] = dp[k_count][i]
                else:
                    max_so_far[k_count][i] = best_of(max_so_far[k_count][i-1], dp[k_count][i])
        
        # Determine the final answer
        final_ans_tuple = (0, []) # Default: 0 intervals, score 0, empty list

        if n > 0:
            for k_chosen in range(1, 5):
                # Best for k_chosen intervals is in max_so_far[k_chosen][n-1]
                if max_so_far[k_chosen][n-1][0] != -1: # Check if valid choice exists
                    final_ans_tuple = best_of(final_ans_tuple, max_so_far[k_chosen][n-1])
        
        return final_ans_tuple[1]