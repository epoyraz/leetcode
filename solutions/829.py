class Solution(object):
    def subdomainVisits(self, cpdomains):
        count = {}
        for entry in cpdomains:
            rep, domain = entry.split()
            rep = int(rep)
            frags = domain.split('.')
            for i in range(len(frags)):
                subdomain = '.'.join(frags[i:])
                count[subdomain] = count.get(subdomain, 0) + rep
        return [str(v) + " " + k for k, v in count.items()]
