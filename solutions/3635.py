from collections import deque

class Solution(object):
    def smallestNumber(self, num, t):
        primes = [2, 3, 5, 7]
        need = []
        for p in primes:
            c = 0
            while t % p == 0:
                t //= p
                c += 1
            need.append(c)
        if t != 1:
            return "-1"
        exp = [(0, 0, 0, 0),
               (0, 0, 0, 0),
               (1, 0, 0, 0),
               (0, 1, 0, 0),
               (2, 0, 0, 0),
               (0, 0, 1, 0),
               (1, 1, 0, 0),
               (0, 0, 0, 1),
               (3, 0, 0, 0),
               (0, 2, 0, 0)]
        need = tuple(need)
        dist = { (0,0,0,0): 0 }
        q = deque([(0,0,0,0)])
        while q:
            a, b, c, d = q.popleft()
            cur = dist[(a,b,c,d)]
            if (a,b,c,d) == need:
                break
            for dig in range(1,10):
                da, db, dc, dd = exp[dig]
                na = min(a+da, need[0])
                nb = min(b+db, need[1])
                nc = min(c+dc, need[2])
                nd = min(d+dd, need[3])
                nxt = (na,nb,nc,nd)
                if nxt not in dist:
                    dist[nxt] = cur+1
                    q.append(nxt)
        if need not in dist:
            return "-1"
        def min_len(v):
            return dist[v]
        def build(v,l):
            res=[]
            for _ in range(l):
                for d in range(1,10):
                    da,db,dc,dd=exp[d]
                    nv=(max(0,v[0]-da),max(0,v[1]-db),max(0,v[2]-dc),max(0,v[3]-dd))
                    if min_len(nv)<=l-len(res)-1:
                        res.append(str(d))
                        v=nv
                        break
            return ''.join(res)
        n=len(num)
        pre_exp=[(0,0,0,0)]
        zero=[False]
        for ch in num:
            d=int(ch)
            e=exp[d] if d else (0,0,0,0)
            pa, pb, pc, pd = pre_exp[-1]
            pre_exp.append((pa+e[0],pb+e[1],pc+e[2],pd+e[3]))
            zero.append(zero[-1] or ch=='0')
        if not zero[-1]:
            pa,pb,pc,pd=pre_exp[-1]
            if pa>=need[0] and pb>=need[1] and pc>=need[2] and pd>=need[3]:
                return num
        for pos in range(n-1,-1,-1):
            if zero[pos]:
                continue
            pa,pb,pc,pd=pre_exp[pos]
            cur=int(num[pos])
            for d in range(cur+1,10):
                if d==0: continue
                da,db,dc,dd=exp[d]
                na=min(pa+da,need[0])
                nb=min(pb+db,need[1])
                nc=min(pc+dc,need[2])
                nd=min(pd+dd,need[3])
                rem_need=(need[0]-na,need[1]-nb,need[2]-nc,need[3]-nd)
                rem=len(num)-pos-1
                if min_len(rem_need)<=rem:
                    tail=build(rem_need,rem)
                    return num[:pos]+str(d)+tail
        total_len=min_len(need)
        L=max(n+1,total_len)
        lead='1'*(L-total_len)
        tail=build(need,total_len)
        return lead+tail
