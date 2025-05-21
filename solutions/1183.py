class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        total_count = sum(count)
        total_sum = 0
        min_val = None
        max_val = None
        mode = 0
        max_freq = 0
        
        # First pass: min, max, sum, mode
        for i in range(256):
            if count[i] > 0:
                if min_val is None:
                    min_val = i
                max_val = i
                total_sum += count[i] * i
                if count[i] > max_freq:
                    max_freq = count[i]
                    mode = i

        # Second pass: find median
        median = 0.0
        mid1 = (total_count + 1) // 2
        mid2 = (total_count + 2) // 2  # Handles both even and odd
        m1 = m2 = None
        curr = 0

        for i in range(256):
            curr += count[i]
            if m1 is None and curr >= mid1:
                m1 = i
            if m2 is None and curr >= mid2:
                m2 = i
                break

        median = (m1 + m2) / 2.0

        return [float(min_val), float(max_val), float(total_sum) / total_count, median, float(mode)]
