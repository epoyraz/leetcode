class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        # Precompute running digit-sums mod 3 and mod 9
        sum3 = [0]*(n+1)
        sum9 = [0]*(n+1)
        for i,ch in enumerate(s):
            d = ord(ch)-48
            sum3[i+1] = (sum3[i] + d) % 3
            sum9[i+1] = (sum9[i] + d) % 9

        # Precompute prefix value mod 7, and 10^t mod7 + their inverses
        pm7 = [0]*(n+1)
        for i,ch in enumerate(s):
            pm7[i+1] = (pm7[i]*10 + (ord(ch)-48)) % 7

        P7 = [1]*6
        for t in range(1,6):
            P7[t] = (P7[t-1]*10) % 7
        # invP7[t] = modular inverse of P7[t] mod 7
        invP7 = [pow(P7[t], 5, 7) for t in range(6)]  # since Ï(7)=6, inv = x^(Ï-1)

        # Counters for substrings by prefixâstate
        cnt3  = [0]*3;  cnt3[0] = 1
        cnt9  = [0]*9;  cnt9[0] = 1
        cnt7  = [[0]*7 for _ in range(6)]
        cnt7[0][0] = 1

        ans = 0
        for j,ch in enumerate(s):
            d = ord(ch) - 48

            if d == 0:
                # substrings ending in '0' are ineligible
                pass

            elif d in (1,2,5):
                # always divisible if last digit is 1,2,5
                ans += (j+1)

            elif d in (3,6):
                # divisible by 3 if digitâsum mod3 matches a previous prefix
                r = sum3[j+1]
                ans += cnt3[r]

            elif d == 9:
                # divisible by 9 if digitâsum mod9 matches
                r = sum9[j+1]
                ans += cnt9[r]

            elif d == 4:
                # divisibility by 4 depends only on the last two digits
                # length=1 always works; length>=2 works if last two %4==0
                add = 1
                if j >= 1:
                    two = ( (ord(s[j-1]) - 48)*10 + 4 )
                    if two % 4 == 0:
                        add += j
                ans += add

            elif d == 8:
                # divisibility by 8 depends on last three digits
                add = 1
                if j >= 1:
                    two = ((ord(s[j-1]) - 48)*10 + 8)
                    if two % 8 == 0:
                        add += 1
                if j >= 2:
                    tri = ((ord(s[j-2]) - 48)*100 +
                           (ord(s[j-1]) - 48)*10 + 8)
                    if tri % 8 == 0:
                        add += (j-1)
                ans += add

            else:  # d == 7
                # use the period-6 trick mod 7
                R = pm7[j+1]
                G = (j+1) % 6
                sub = 0
                for r_mod in range(6):
                    t = (G - r_mod) % 6
                    need = (R * invP7[t]) % 7
                    sub += cnt7[r_mod][need]
                ans += sub

            # --- now update the prefix-state counters at position j+1 ---
            cnt3[ sum3[j+1] ] += 1
            cnt9[ sum9[j+1] ] += 1
            km = (j+1) % 6
            rv = pm7[j+1]
            cnt7[km][rv] += 1

        return ans
