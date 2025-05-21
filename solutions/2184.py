from collections import deque

class Solution:
    def possiblyEquals(self, s1, s2):
        """
        Returns True if there exists an original string that can be encoded
        as both s1 and s2 according to the described rules.
        """
        N1, N2 = len(s1), len(s2)
        # BFS state: (i, j, diff)
        seen = set()
        dq = deque([(0, 0, 0)])
        seen.add((0, 0, 0))
        
        while dq:
            i, j, diff = dq.popleft()
            # If both strings consumed and balanced, success
            if i == N1 and j == N2 and diff == 0:
                return True
            
            # diff == 0: align new letters or introduce skips
            if diff == 0:
                # match letters
                if i < N1 and j < N2 and s1[i].isalpha() and s2[j].isalpha():
                    if s1[i] == s2[j]:
                        state = (i+1, j+1, 0)
                        if state not in seen:
                            seen.add(state)
                            dq.append(state)
                # skip via number in s1
                if i < N1 and s1[i].isdigit():
                    num = 0
                    for k in range(i, min(N1, i+3)):
                        if s1[k].isdigit():
                            num = num*10 + int(s1[k])
                            state = (k+1, j, diff + num)
                            if state not in seen:
                                seen.add(state)
                                dq.append(state)
                        else:
                            break
                # skip via number in s2
                if j < N2 and s2[j].isdigit():
                    num = 0
                    for k in range(j, min(N2, j+3)):
                        if s2[k].isdigit():
                            num = num*10 + int(s2[k])
                            state = (i, k+1, diff - num)
                            if state not in seen:
                                seen.add(state)
                                dq.append(state)
                        else:
                            break
            
            # diff > 0: s1 is ahead, consume from s2
            elif diff > 0:
                # consume a letter from s2
                if j < N2 and s2[j].isalpha():
                    state = (i, j+1, diff-1)
                    if state not in seen:
                        seen.add(state)
                        dq.append(state)
                # consume via number in s2
                if j < N2 and s2[j].isdigit():
                    num = 0
                    for k in range(j, min(N2, j+3)):
                        if s2[k].isdigit():
                            num = num*10 + int(s2[k])
                            state = (i, k+1, diff - num)
                            if state not in seen:
                                seen.add(state)
                                dq.append(state)
                        else:
                            break
            
            # diff < 0: s2 is ahead, consume from s1
            else:
                # consume a letter from s1
                if i < N1 and s1[i].isalpha():
                    state = (i+1, j, diff+1)
                    if state not in seen:
                        seen.add(state)
                        dq.append(state)
                # consume via number in s1
                if i < N1 and s1[i].isdigit():
                    num = 0
                    for k in range(i, min(N1, i+3)):
                        if s1[k].isdigit():
                            num = num*10 + int(s1[k])
                            state = (k+1, j, diff + num)
                            if state not in seen:
                                seen.add(state)
                                dq.append(state)
                        else:
                            break
        
        return False
