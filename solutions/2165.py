class Solution:
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        
        # 1) prefix_stars[i]: number of '*' in s[0..i-1]
        prefix_stars = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            prefix_stars[i] = prefix_stars[i - 1] + (ch == '*')
        
        # 2) nearest candle to the left of or at i
        left_candle = [-1] * n
        last = -1
        for i, ch in enumerate(s):
            if ch == '|':
                last = i
            left_candle[i] = last
        
        # 3) nearest candle to the right of or at i
        right_candle = [-1] * n
        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last = i
            right_candle[i] = last
        
        ans = []
        for l, r in queries:
            # find the span [a,b] of full candle-to-candle inside [l,r]
            a = right_candle[l]
            b = left_candle[r]
            
            # valid only if there are two candles and a < b
            if a != -1 and b != -1 and a < b:
                # plates between a and b = stars up to b minus stars up to a
                count = prefix_stars[b] - prefix_stars[a]
                ans.append(count)
            else:
                ans.append(0)
        
        return ans
