class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        n = len(energy)
        energy_needed = max(0, sum(energy) - initialEnergy + 1)
        exp_needed = 0
        curr_exp = initialExperience

        for i in range(n):
            if curr_exp <= experience[i]:
                extra = experience[i] - curr_exp + 1
                exp_needed += extra
                curr_exp += extra
            curr_exp += experience[i]

        return energy_needed + exp_needed
