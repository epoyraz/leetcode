class Solution(object):
    def longestPalindrome(self, s, t):
        s_N = len(s)
        t_N = len(t)

        # Since s.length, t.length >= 1, min palindrome is 1 char
        max_overall_len = 1
        
        # --- Step 2: Precompute is_palindrome and find longest palindrome in s and t individually ---
        is_palindrome_s = [[False for _ in range(s_N)] for _ in range(s_N)]
        for length in range(1, s_N + 1):
            for r_idx in range(s_N - length + 1): # r_idx is start_idx
                c_idx = r_idx + length - 1 # c_idx is end_idx
                if length == 1:
                    is_palindrome_s[r_idx][c_idx] = True
                elif length == 2:
                    is_palindrome_s[r_idx][c_idx] = (s[r_idx] == s[c_idx])
                else:
                    is_palindrome_s[r_idx][c_idx] = (s[r_idx] == s[c_idx] and is_palindrome_s[r_idx+1][c_idx-1])
                
                if is_palindrome_s[r_idx][c_idx]:
                    max_overall_len = max(max_overall_len, length)

        is_palindrome_t = [[False for _ in range(t_N)] for _ in range(t_N)]
        for length in range(1, t_N + 1):
            for r_idx in range(t_N - length + 1): # r_idx is start_idx
                c_idx = r_idx + length - 1 # c_idx is end_idx
                if length == 1:
                    is_palindrome_t[r_idx][c_idx] = True
                elif length == 2:
                    is_palindrome_t[r_idx][c_idx] = (t[r_idx] == t[c_idx])
                else:
                    is_palindrome_t[r_idx][c_idx] = (t[r_idx] == t[c_idx] and is_palindrome_t[r_idx+1][c_idx-1])

                if is_palindrome_t[r_idx][c_idx]:
                    max_overall_len = max(max_overall_len, length)
        
        # --- Step 3: Precompute max_len_pal_s_starting_at ---
        max_len_pal_s_starting_at = [0] * (s_N + 1) # index s_N for empty palindrome (len 0)
        if s_N > 0: # Only if s is not empty
            for k in range(s_N):
                current_max_len_for_k = 0
                for x in range(k, s_N): # x is end_idx
                    if is_palindrome_s[k][x]:
                        current_max_len_for_k = max(current_max_len_for_k, x - k + 1)
                max_len_pal_s_starting_at[k] = current_max_len_for_k
        
        # --- Step 4: Precompute max_len_pal_t_ending_at ---
        # Array index `idx_fixed = original_end_idx + 1`. `idx_fixed = 0` for empty palindrome.
        max_len_pal_t_ending_at_fixed = [0] * (t_N + 1)
        if t_N > 0: # Only if t is not empty
            for k in range(t_N): # k is end_idx
                current_max_len_for_k = 0
                for x in range(k + 1): # x is start_idx
                    if is_palindrome_t[x][k]:
                        current_max_len_for_k = max(current_max_len_for_k, k - x + 1)
                max_len_pal_t_ending_at_fixed[k+1] = current_max_len_for_k

        # --- Step 5: Reverse t ---
        t_r = t[::-1]

        # --- Step 6: Compute LCP_lengths table ---
        LCP_lengths = [[0 for _ in range(t_N + 1)] for _ in range(s_N + 1)]
        if s_N > 0 and t_N > 0: # Only if both s and t_r (i.e. t) are non-empty
            for r_idx in range(s_N - 1, -1, -1): # start_idx in s
                for c_idx in range(t_N - 1, -1, -1): # start_idx in t_r
                    if s[r_idx] == t_r[c_idx]:
                        LCP_lengths[r_idx][c_idx] = LCP_lengths[r_idx+1][c_idx+1] + 1
                    # else, LCP_lengths[r_idx][c_idx] remains 0 (from initialization)
        
        # --- Step 7: Iterate, calculate, and update max_overall_len ---
        if s_N > 0 and t_N > 0: # Only if both s and t are non-empty for Case 3
            for r_idx in range(s_N): # r_idx is start index i of A in s
                for c_idx in range(t_N): # c_idx is start index j of A^rev in t_r
                    L = LCP_lengths[r_idx][c_idx]
                    if L == 0: # A must be non-empty
                        continue

                    # Case 3a: W = A A_t^rev. Length = 2*L
                    max_overall_len = max(max_overall_len, 2 * L)

                    # Case 3b: W = A P_s A_t^rev
                    # P_s starts at s[r_idx+L].
                    idx_ps_starts = r_idx + L 
                    # max_len_pal_s_starting_at[s_N] is 0, handles P_s being empty.
                    len_ps = max_len_pal_s_starting_at[idx_ps_starts] 
                    max_overall_len = max(max_overall_len, 2 * L + len_ps)
                    
                    # Case 3c: W = A P_t A_t^rev
                    # A_t in original t is t[t_N-c_idx-L ... t_N-c_idx-1]
                    # P_t ends at index (t_N-c_idx-L) - 1 in original t.
                    idx_pt_ends = t_N - c_idx - L - 1
                    # map to fixed array index: (idx_pt_ends) + 1.
                    # if idx_pt_ends = -1 (P_t empty), then fixed_idx = 0, gives len_pt=0.
                    len_pt = max_len_pal_t_ending_at_fixed[idx_pt_ends + 1]
                    max_overall_len = max(max_overall_len, 2 * L + len_pt)
                
        return max_overall_len