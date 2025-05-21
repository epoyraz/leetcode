class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Count initial active sections
        total_ones = s.count('1')
        
        # Build segments of t = '1' + s + '1'
        segments = []
        curr_char = '1'
        curr_len = 1
        # Process s
        for c in s:
            if c == curr_char:
                curr_len += 1
            else:
                segments.append((curr_char, curr_len))
                curr_char = c
                curr_len = 1
        # Process trailing '1'
        if curr_char == '1':
            curr_len += 1
        else:
            segments.append((curr_char, curr_len))
            curr_char = '1'
            curr_len = 1
        segments.append((curr_char, curr_len))
        
        # Compute max gain = z_left + z_right for each removable '1'-segment
        max_gain = 0
        m = len(segments)
        # We can pick any '1'-segment at index i with zeros on both sides => i in [1..m-2]
        for i in range(1, m-1):
            typ, length = segments[i]
            if typ == '1':
                # neighbors must be zeros by construction of t
                z_left = segments[i-1][1]
                z_right = segments[i+1][1]
                gain = z_left + z_right
                if gain > max_gain:
                    max_gain = gain
        
        # Best we can do
        return total_ones + max_gain
