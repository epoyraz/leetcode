class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        n = len(nums)

        # Group queries by right endpoint
        qs_by_r = [[] for _ in range(n)]
        for qi, (l, r) in enumerate(queries):
            qs_by_r[r].append((l, qi))
        answer = [0] * len(queries)

        # prev_diag will hold f[i][(d-1)-i] for i=0..d-1
        prev_diag = []

        # prev_best[l] will be the maximum score for any subarray
        # inside [l..d-1], so we can extend it to [l..d].
        prev_best = []

        # Process diagonals d=0..n-1, which correspond to subarrays ending at r=d
        for d in range(n):
            # Build current diagonal: f[i][d-i] for i=0..d
            cur_diag = [0] * (d + 1)
            # Fill from i=d down to 0 so cur_diag[i+1] is ready when needed
            for i in range(d, -1, -1):
                length_minus1 = d - i  # this is m-1 where m = length
                if length_minus1 == 0:
                    # subarray of length 1
                    cur_diag[i] = nums[i]
                else:
                    # recurrence f(i,m) = f(i,m-1) XOR f(i+1,m-1)
                    cur_diag[i] = prev_diag[i] ^ cur_diag[i+1]

            # Compute suffix-max of cur_diag so
            # end_max[i] = max_{start â¥ i, end=d} score(start..d)
            end_max = [0] * (d + 1)
            for i in range(d, -1, -1):
                if i == d:
                    end_max[i] = cur_diag[i]
                else:
                    end_max[i] = max(cur_diag[i], end_max[i+1])

            # Build the new best array for subarrays in [l..d]
            new_best = [0] * (d + 1)
            for l in range(d, -1, -1):
                if l == d:
                    # only one subarray [d..d]
                    new_best[l] = cur_diag[l]
                else:
                    # either we take the best entirely within [l..d-1],
                    # or we take one that ends exactly at d (captured in end_max[l])
                    new_best[l] = max(prev_best[l], end_max[l])

            # Answer all queries with right endpoint = d
            for (l, qi) in qs_by_r[d]:
                answer[qi] = new_best[l]

            # Slide the window: current becomes previous for the next diagonal
            prev_diag = cur_diag
            prev_best = new_best

        return answer
