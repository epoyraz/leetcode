class Solution:
    def numUniqueEmails(self, emails):
        seen = set()

        for email in emails:
            local, domain = email.split('@')
            # Ignore everything after first '+' and remove all '.'
            local = local.split('+')[0].replace('.', '')
            normalized = local + '@' + domain
            seen.add(normalized)

        return len(seen)
