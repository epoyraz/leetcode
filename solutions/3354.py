import heapq

class Solution(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1) Count initial letters and '?' count
        a = [0]*26
        q = 0
        for ch in s:
            if ch == '?':
                q += 1
            else:
                a[ord(ch) - 97] += 1
        
        # 2) Compute b[i]: how many '?' to assign to letter i
        heap = [(a[i], i) for i in range(26)]
        heapq.heapify(heap)
        b = [0]*26
        for _ in range(q):
            c, i = heapq.heappop(heap)
            b[i] += 1
            heapq.heappush(heap, (c+1, i))
        
        # 3) Reconstruct the answer lexicographically
        res = []
        for ch in s:
            if ch != '?':
                res.append(ch)
            else:
                # pick smallest i with b[i]>0
                for i in range(26):
                    if b[i] > 0:
                        b[i] -= 1
                        res.append(chr(97 + i))
                        break
        
        return "".join(res)
