class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Make sure both nodes are initialized
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if y not in self.parent:
            self.parent[y] = y
            self.rank[y] = 0

        # Find roots
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return

        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

class Solution(object):
    def accountsMerge(self, accounts):
        uf = UnionFind()
        email_to_name = {}

        # 1) Union emails in the same account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                # Map email to user name
                email_to_name[email] = name
                # Union this email with the first email in account
                uf.union(first_email, email)

        # 2) Group emails by their root parent
        from collections import defaultdict
        groups = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            groups[root].append(email)

        # 3) Build the merged account list
        result = []
        for root, emails in groups.items():
            name = email_to_name[root]
            emails.sort()
            result.append([name] + emails)

        return result
