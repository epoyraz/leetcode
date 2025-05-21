from collections import defaultdict

class ThroneInheritance:
    def __init__(self, kingName):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName, childName):
        # add new child at the end of the parentâs list
        self.children[parentName].append(childName)

    def death(self, name):
        # just mark dead; we still traverse them in the tree
        self.dead.add(name)

    def getInheritanceOrder(self):
        order = []
        # preorder DFS
        def dfs(name):
            if name not in self.dead:
                order.append(name)
            for c in self.children[name]:
                dfs(c)

        dfs(self.king)
        return order
