class Solution(object):
    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        n = len(arr)
        
        # 1) Precompute the substring sets for each string
        subs = []
        for s in arr:
            st = set()
            L = len(s)
            for i in range(L):
                for j in range(i+1, L+1):
                    st.add(s[i:j])
            subs.append(st)
        
        answer = []
        
        # 2) For each string, find its shortest unique substring
        for i, s in enumerate(arr):
            L = len(s)
            found = ""
            # try each length
            for length in range(1, L+1):
                # collect all substrings of this length, sorted
                cand = sorted({s[j:j+length] for j in range(0, L-length+1)})
                for t in cand:
                    # check if t occurs in any other string
                    ok = True
                    for j in range(n):
                        if j == i: continue
                        if t in subs[j]:
                            ok = False
                            break
                    if ok:
                        found = t
                        break
                if found:
                    break
            
            answer.append(found)
        
        return answer
