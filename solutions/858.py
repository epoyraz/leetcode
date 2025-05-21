class Solution(object):
    def maskPII(self, s):
        if '@' in s:
            name, domain = s.lower().split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:
            digits = [c for c in s if c.isdigit()]
            local = "***-***-" + ''.join(digits[-4:])
            if len(digits) == 10:
                return local
            else:
                return "+" + "*" * (len(digits) - 10) + "-" + local
