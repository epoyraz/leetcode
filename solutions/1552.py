class Solution:
    def buildArray(self, target, n):
        result = []
        current = 1
        for num in target:
            while current < num:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1
        return result
