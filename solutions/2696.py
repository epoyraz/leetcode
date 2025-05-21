from collections import Counter, defaultdict

class Solution:
    def beautifulSubsets(self, nums, k):
        # Group numbers by modulo k to separate independent buckets
        buckets = defaultdict(list)
        for x in nums:
            buckets[x % k].append(x)

        total_sets = 1
        # Process each bucket independently
        for arr in buckets.values():
            cnt = Counter(arr)
            # Sort unique values
            values = sorted(cnt)

            # dp_no: ways for prefix without taking previous value
            # dp_yes: ways for prefix with taking previous value
            dp_no, dp_yes = 1, 0
            prev = None
            for v in values:
                c = cnt[v]
                # number of non-empty ways to choose from duplicates of v
                take_ways = (1 << c) - 1

                # Check if current value conflicts with previous (difference == k)
                if prev is not None and v - prev == k:
                    # Conflict: can only take v if previous was not taken
                    new_dp_yes = dp_no * take_ways
                else:
                    # No conflict: can take v regardless of previous
                    new_dp_yes = (dp_no + dp_yes) * take_ways

                # Whether we take v or not, the 'no' state accumulates all previous
                new_dp_no = dp_no + dp_yes

                dp_no, dp_yes = new_dp_no, new_dp_yes
                prev = v

            # Total subsets for this bucket = all 'yes' and 'no' states
            bucket_total = dp_no + dp_yes
            total_sets *= bucket_total

        # Subtract the empty subset
        return total_sets - 1