class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.n = len(parent)
        self.children = [[] for _ in range(self.n)]
        for i in range(1, self.n):
            self.children[parent[i]].append(i)
        self.locked_by = [-1] * self.n  # -1 means unlocked

    def lock(self, num, user):
        if self.locked_by[num] != -1:
            return False
        self.locked_by[num] = user
        return True

    def unlock(self, num, user):
        if self.locked_by[num] != user:
            return False
        self.locked_by[num] = -1
        return True

    def upgrade(self, num, user):
        # Check condition 1: node must be unlocked
        if self.locked_by[num] != -1:
            return False

        # Check condition 2: has at least one locked descendant
        if not self._has_locked_descendant(num):
            return False

        # Check condition 3: no locked ancestor
        if self._has_locked_ancestor(num):
            return False

        # Unlock all descendants
        self._unlock_all_descendants(num)

        # Lock the current node
        self.locked_by[num] = user
        return True

    def _has_locked_descendant(self, node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for child in self.children[curr]:
                if self.locked_by[child] != -1:
                    return True
                stack.append(child)
        return False

    def _has_locked_ancestor(self, node):
        while node != -1:
            if self.locked_by[node] != -1:
                return True
            node = self.parent[node]
        return False

    def _unlock_all_descendants(self, node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for child in self.children[curr]:
                self.locked_by[child] = -1
                stack.append(child)
