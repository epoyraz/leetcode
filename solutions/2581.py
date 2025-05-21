class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        target = skill[0] + skill[-1]
        chemistry = 0
        i, j = 0, len(skill) - 1
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        return chemistry
